import unreal

actors = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in actors:
    instanced_static_mesh = actor.root_component
    count = instanced_static_mesh.get_instance_count()
    static_mesh = instanced_static_mesh.static_mesh
    for num in range(count):
        location = instanced_static_mesh.get_instance_transform(num).translation
        rotation = instanced_static_mesh.get_instance_transform(num).rotation.rotator()
        scale = instanced_static_mesh.get_instance_transform(num).scale3d
        new_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(static_mesh, location, rotation)
        new_actor.set_actor_scale3d(scale)

    unreal.log(static_mesh)
    option = unreal.EditorScriptingJoinStaticMeshActorsOptions()
    

unreal.log('------------------------')