# Development notes

## Initial setup

- Engine: Unreal Engine 5.8.3; the project association is `5.8`.
- Start with Blueprints; choose the C++ boundary when gameplay systems require it.
- Keep game-owned assets under `/Game/AFlagOfYourOwn`.
- Use Git LFS for `.uasset`, `.umap`, and source art covered by `.gitattributes`.
- Commit `Config/Default*.ini`; leave generated caches and local settings ignored.
- Do not rename an asset by moving its file in Explorer. Rename it in Unreal and fix redirectors.

## Content organization

Create folders as they acquire assets: `Blueprints`, `Characters`, `Data`, `Environment`, `Maps`, `Materials`, `Ships`, and `UI`.

Use `BP_` for Blueprints, `L_` for maps, `WBP_` for widgets, `M_` for materials, `MI_` for material instances, `SM_` for static meshes, and `DA_` for data assets. Prefer descriptive names over numbered placeholders.

## Prototype map utility

`Tools/Editor/create_prototype_map.py` creates the harbor blockout using Unreal's built-in shapes. It is an editor utility and never runs during gameplay or automatically on startup. It refuses to overwrite an existing map.

To recreate a missing map on Windows, run this from the repository root in PowerShell, adjusting the engine path for your installation:

```powershell
& 'C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe' `
    (Join-Path $PWD 'AFlagOfYourOwn.uproject') `
    -run=pythonscript `
    '-script=Tools/Editor/create_prototype_map.py' `
    -unattended -nullrhi -nosplash -nosound
```

## Proposed first playable milestone

- [ ] Choose the player perspective and add a controllable character.
- [ ] Add one shipboard interaction and one chore with a clear completion condition.
- [ ] Track pay and reputation and display the reward.
- [ ] Save and load the player's earned progress.
- [ ] Playtest the full chore loop in the packaged Windows build.

The initial flying pawn is a layout inspection tool. No movement, interaction, progression, or saving system should be marked complete based on this scaffold.

## Repeatable Unreal smoke test

Run from the repository root with Python 3. It launches a separate Unreal 5.8.3 commandlet with NullRHI, reads project assets and configured maps, and checks that the gameplay map has a PlayerStart and assigned static mesh geometry. It never saves or creates content assets.

```shell
python Tools/Editor/run_smoke_test.py
```

For another installation path, pass `--engine-dir "D:/Epic Games/UE_5.8"` or set `UE_ENGINE_DIR`. `--timeout` limits engine runtime in seconds (default 600). Each run writes `result.json`, `engine.log` and `console.log` into a new `Saved/SmokeTests/<run-id>/` directory, ignored by Git. The JSON records engine version, loaded maps, asset counts, PlayerStarts and errors. A nonzero exit, missing report, mismatched run/project or failed check makes the wrapper fail; an old success report cannot satisfy a new run.

To check the failure path deliberately, this command must return exit code 1 with a missing-map error in its report:

```shell
python Tools/Editor/run_smoke_test.py --map /Game/AFlagOfYourOwn/Maps/L_DoesNotExist
```

This is a loadability check. It does not validate Blueprint compilation, camera controls, Play, rendering, fun or packaging. Those checks remain required on the relevant gameplay issues and the Windows MVP milestone. Hosted CI tests the report handling; the full engine check requires the local Unreal installation.
