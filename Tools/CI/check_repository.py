"""Fast repository checks; does not run Unreal or validate gameplay."""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
LFS_EXTENSIONS = {'.uasset', '.umap', '.fbx', '.blend', '.wav', '.png', '.tga', '.exr',
                  '.psd', '.tif', '.tiff', '.jpg', '.jpeg', '.ogg', '.mp3', '.mp4'}
GENERATED = {'Saved', 'Intermediate', 'DerivedDataCache', 'Binaries', '.vs', '__pycache__'}
POINTER = re.compile(rb'version https://git-lfs.github.com/spec/v1\noid sha256:[0-9a-f]{64}\nsize [0-9]+\n')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def main():
    errors = []
    files = git('ls-files', '-z').decode().split('\0')
    files = [name for name in files if name]
    project = json.loads((ROOT / 'AFlagOfYourOwn.uproject').read_text(encoding='utf-8'))
    if project.get('EngineAssociation') != '5.8':
        errors.append('EngineAssociation must remain 5.8 until an explicit engine upgrade.')
    for name in files:
        path = Path(name)
        parts = path.parts
        if any(part in GENERATED for part in parts) or path.suffix in {'.pyc', '.pyo'}:
            errors.append(f'Generated file tracked: {name}')
        if path.name.startswith('.env') and path.name != '.env.example':
            errors.append(f'Local environment file tracked: {name}')
        if path.suffix == '.py':
            try:
                ast.parse((ROOT / path).read_text(encoding='utf-8'), filename=name)
            except (SyntaxError, UnicodeError) as exc:
                errors.append(f'Invalid Python: {name}: {exc}')
        if path.suffix == '.json':
            try:
                json.loads((ROOT / path).read_text(encoding='utf-8'))
            except (ValueError, UnicodeError) as exc:
                errors.append(f'Invalid JSON: {name}: {exc}')
        if path.suffix.lower() in LFS_EXTENSIONS:
            attribute = git('check-attr', '--cached', 'filter', '--', name).decode().strip()
            if not attribute.endswith(': lfs'):
                errors.append(f'Binary asset lacks LFS filter: {name}')
            size = int(git('cat-file', '-s', ':' + name))
            if size > 1024 or not POINTER.fullmatch(git('show', ':' + name)):
                errors.append(f'Binary asset is not a canonical LFS pointer in Git index: {name}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Repository checks passed ({len(files)} tracked files). Unreal checks remain separate.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
