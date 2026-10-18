# A Flag of Your Own

A pirate life sim where you rise from deckhand to captain, manage ships and crews, and command a growing fleet from your own island estate.

## Project status

Initial Unreal Engine **5.8.3** project, starting with Blueprints. The repository contains project settings, a small harbor blockout, and the initial design direction. Sailing, crew management, career progression, fleets, and estates are planned features, not implemented systems.

The harbor uses engine primitives for a shore platform, pier, and stationary ship deck. Play currently uses Unreal's default flying pawn to inspect the layout; this is not the final player controller or camera.

## Open the project

1. Install Unreal Engine **5.8.3** and Git LFS.
2. Clone the repository and fetch its binary assets:

   ```shell
   git clone https://github.com/CourteousWinter/A-Flag-of-Your-Own.git
   cd A-Flag-of-Your-Own
   git lfs install --local
   git lfs pull
   ```

3. Open `AFlagOfYourOwn.uproject` in Unreal Editor.
4. The editor opens `L_PrototypeHarbor`. Press **Play** to inspect it. Click the viewport, use **WASD** and the mouse to fly, and **Esc** to stop.

The first launch may take time while Unreal builds its local shader cache. The project currently has no native C++ module, so a C++ compiler is not required to open it.

## Repository layout

```text
AFlagOfYourOwn.uproject       Unreal project descriptor
Config/                      Shared project settings
Content/AFlagOfYourOwn/       Game-owned assets and prototype map
Docs/                        Vision and development notes
Tools/Editor/                Explicitly run editor utilities
```

Read [the game vision](Docs/Vision.md) for the concept and [development notes](Docs/Development.md) for asset conventions and the proposed first playable milestone.
