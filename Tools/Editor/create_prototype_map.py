"""Create a small, non-destructive harbor blockout inside Unreal Editor."""

import unreal


MAP_PATH = "/Game/AFlagOfYourOwn/Maps/L_PrototypeHarbor"


def create_map():
    assets = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    if assets.does_asset_exist(MAP_PATH):
        raise RuntimeError(f"Refusing to overwrite an existing map: {MAP_PATH}")

    levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if not levels.new_level(MAP_PATH):
        raise RuntimeError(f"Could not create {MAP_PATH}")

    cube = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
    cylinder = unreal.load_asset("/Engine/BasicShapes/Cylinder.Cylinder")
    if not cube or not cylinder:
        raise RuntimeError("Required Unreal Engine basic shapes are missing.")

    def spawn(actor_class, label, location, rotation=(0, 0, 0), folder="Blockout"):
        actor = actors.spawn_actor_from_class(
            actor_class, unreal.Vector(*location), unreal.Rotator(*rotation)
        )
        if not actor:
            raise RuntimeError(f"Could not spawn {label}")
        actor.set_actor_label(label)
        actor.set_folder_path(folder)
        return actor

    def shape(label, location, scale, mesh=cube, folder="Blockout"):
        actor = spawn(unreal.StaticMeshActor, label, location, folder=folder)
        component = actor.get_component_by_class(unreal.StaticMeshComponent)
        component.set_static_mesh(mesh)
        actor.set_actor_scale3d(unreal.Vector(*scale))
        return actor

    # Unreal units are centimeters; these are layout guides, not final art.
    shape("Shore_Platform", (-1800, 0, -75), (30, 50, 1.5))
    shape("Pier_Deck", (700, 0, -25), (20, 4, 0.5))
    for index, x in enumerate((0, 700, 1400)):
        for side in (-1, 1):
            shape(
                f"Pier_Post_{index}_{'L' if side < 0 else 'R'}",
                (x, side * 150, -200),
                (0.3, 0.3, 4),
                cylinder,
            )

    shape("Ship_Deck_Placeholder", (900, 750, -15), (18, 6, 0.5), folder="Ship")
    shape("Ship_Cabin_Placeholder", (250, 750, 135), (4, 5, 2.5), folder="Ship")
    shape("Ship_Mast_Placeholder", (1000, 750, 450), (0.3, 0.3, 9), cylinder, "Ship")
    shape("Ship_Rail_Port", (900, 1040, 45), (18, 0.2, 0.8), folder="Ship")
    shape("Ship_Rail_Starboard", (900, 460, 45), (18, 0.2, 0.8), folder="Ship")

    sun = spawn(
        unreal.DirectionalLight, "Sun", (0, 0, 2000), (-40, -30, 0), "Lighting"
    )
    sun_component = sun.get_component_by_class(unreal.DirectionalLightComponent)
    sun_component.set_editor_property("atmosphere_sun_light", True)
    sun_component.set_editor_property("intensity", 5.0)
    spawn(unreal.SkyAtmosphere, "Sky_Atmosphere", (0, 0, 0), folder="Lighting")
    sky = spawn(unreal.SkyLight, "Sky_Light", (0, 0, 1500), folder="Lighting")
    sky.get_component_by_class(unreal.SkyLightComponent).set_editor_property(
        "real_time_capture", True
    )
    spawn(unreal.PlayerStart, "Player_Start", (-1200, 0, 200), folder="Gameplay")

    if not levels.save_current_level():
        raise RuntimeError(f"Could not save {MAP_PATH}")
    unreal.log(f"AFYO_BOOTSTRAP_OK: saved {MAP_PATH}")


if __name__ == "__main__":
    create_map()
