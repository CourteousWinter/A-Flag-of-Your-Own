"""Run the project's read-only Unreal validation with per-run evidence."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / 'AFlagOfYourOwn.uproject'


def read_result(report_path, run_id, project, engine_exit):
    """Reject false success from a failed engine, absent/stale or unrelated report."""
    if engine_exit != 0:
        raise ValueError(f'Unreal exited with code {engine_exit}; inspect engine.log and console.log.')
    try:
        result = json.loads(report_path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ValueError(f'Missing or invalid report: {report_path}') from exc
    if not isinstance(result, dict) or result.get('run_id') != run_id:
        raise ValueError('Report does not belong to this run.')
    reported_project = result.get('project')
    if not isinstance(reported_project, str) or not reported_project:
        raise ValueError('Report has no valid project path.')
    if os.path.normcase(str(Path(reported_project).resolve())) != os.path.normcase(str(project.resolve())):
        raise ValueError('Report belongs to a different project.')
    if result.get('status') != 'passed' or result.get('errors') != []:
        raise ValueError(f'Unreal validation failed: {result.get("errors", [])}')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine-dir', type=Path,
                        default=Path(os.environ.get('UE_ENGINE_DIR', 'C:/Program Files/Epic Games/UE_5.8')))
    parser.add_argument('--map', help='Override the map to inspect, e.g. for a negative validation test.')
    parser.add_argument('--timeout', type=int, default=600, help='Engine timeout in seconds (default: 600).')
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('--timeout must be positive')
    editor = args.engine_dir / 'Engine/Binaries/Win64/UnrealEditor-Cmd.exe'
    if not editor.is_file():
        print(f'UnrealEditor-Cmd.exe not found: {editor}', file=sys.stderr)
        return 1
    run_id = uuid.uuid4().hex
    output = ROOT / 'Saved/SmokeTests' / run_id
    output.mkdir(parents=True)
    report = output / 'result.json'
    environment = {**os.environ, 'AFYO_SMOKE_RUN_ID': run_id,
                   'AFYO_SMOKE_REPORT': str(report), 'AFYO_SMOKE_MAP': args.map or ''}
    command = [str(editor), str(PROJECT), '-run=pythonscript',
               f'-script={ROOT / "Tools/Editor/validate_project.py"}',
               '-unattended', '-nullrhi', '-nosplash', '-nosound', '-nop4',
               '-stdout', '-FullStdOutLogOutput', f'-abslog={output / "engine.log"}']
    print(f'Unreal smoke test evidence: {output}', flush=True)
    try:
        with (output / 'console.log').open('w', encoding='utf-8') as log:
            process = subprocess.run(command, cwd=ROOT, env=environment, stdout=log,
                                     stderr=subprocess.STDOUT, timeout=args.timeout, check=False)
        result = read_result(report, run_id, PROJECT, process.returncode)
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        print(f'Evidence: {output}', file=sys.stderr)
        return 1
    print(f'PASS: Unreal {result["engine_version"]}; {result["asset_count"]} game assets; '
          f'{result["player_starts"]} PlayerStart(s); {result["mesh_components"]} static mesh component(s).')
    print(f'Report: {report}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
