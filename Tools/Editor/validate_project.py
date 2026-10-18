"""Read-only Unreal commandlet validation; invoke through run_smoke_test.py."""
import configparser
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import traceback

import unreal


def main():
    project_dir = Path(unreal.Paths.convert_relative_path_to_full(unreal.Paths.project_dir())).resolve()
    project = project_dir / 'AFlagOfYourOwn.uproject'
    run_id = os.environ['AFYO_SMOKE_RUN_ID']
    report_path = Path(os.environ['AFYO_SMOKE_REPORT']).resolve()
    if not report_path.is_relative_to(project_dir / 'Saved/SmokeTests'):
        raise RuntimeError('Validation evidence must be written under Saved/SmokeTests.')
    result = {'run_id': run_id, 'project': str(project),
              'started_at': datetime.now(timezone.utc).isoformat(),
              'engine_version': unreal.SystemLibrary.get_engine_version(),
              'status': 'failed', 'errors': [], 'loaded_maps': [],
              'asset_count': 0, 'player_starts': 0, 'mesh_components': 0}
    try:
        if not result['engine_version'].startswith('5.8.3-'):
            raise RuntimeError(f'Expected Unreal 5.8.3, got {result["engine_version"]}')
        descriptor = json.loads(project.read_text(encoding='utf-8'))
        if descriptor.get('EngineAssociation') != '5.8':
            raise RuntimeError('Project association must be 5.8.')
        config = configparser.ConfigParser(interpolation=None, strict=False)
        config.optionxform = str
        config.read(project_dir / 'Config/DefaultEngine.ini', encoding='utf-8')
        settings = config['/Script/EngineSettings.GameMapsSettings']
        override = os.environ.get('AFYO_SMOKE_MAP')
        editor_map = override or settings['EditorStartupMap'].strip('"')
        game_map = override or settings['GameDefaultMap'].strip('"')
        maps = list(dict.fromkeys([editor_map, game_map]))

        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        registry.search_all_assets(True)
        assets = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
        actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        owned_assets = assets.list_assets('/Game/AFlagOfYourOwn', True, False)
        if not owned_assets:
            raise RuntimeError('No game-owned assets found under /Game/AFlagOfYourOwn.')
        for asset_path in owned_assets:
            if not assets.load_asset(asset_path):
                raise RuntimeError(f'Could not load game asset: {asset_path}')
        result['asset_count'] = len(owned_assets)

        for map_path in maps:
            if not map_path.startswith('/Game/') or not assets.does_asset_exist(map_path):
                raise RuntimeError(f'Configured map is missing or unresolved: {map_path}')
            if not levels.load_level(map_path):
                raise RuntimeError(f'Could not open configured map: {map_path}')
            result['loaded_maps'].append(map_path)
        level_actors = actors.get_all_level_actors()
        result['player_starts'] = sum(isinstance(actor, unreal.PlayerStart) for actor in level_actors)
        if not result['player_starts']:
            raise RuntimeError('Gameplay map has no PlayerStart.')
        for actor in level_actors:
            for component in actor.get_components_by_class(unreal.StaticMeshComponent):
                result['mesh_components'] += 1
                if not component.get_editor_property('static_mesh'):
                    raise RuntimeError(f'Missing static mesh on actor: {actor.get_actor_label()}')
        if not result['mesh_components']:
            raise RuntimeError('Gameplay map has no static mesh geometry.')
        result['status'] = 'passed'
    except Exception as exc:
        result['errors'].append(str(exc))
        unreal.log_error(traceback.format_exc())
    finally:
        result['finished_at'] = datetime.now(timezone.utc).isoformat()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = report_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        temporary.replace(report_path)
    if result['status'] != 'passed':
        raise RuntimeError('AFYO_SMOKE_FAILED: ' + '; '.join(result['errors']))
    unreal.log('AFYO_SMOKE_PASSED: ' + str(report_path))


if __name__ == '__main__':
    main()
