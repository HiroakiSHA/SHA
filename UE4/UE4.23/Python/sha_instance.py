import unreal

def reverse_instance():
    actors = unreal.EditorLevelLibrary.get_selected_level_actors()

    for actor in actors:
        root_component = actor.root_component
        all_component = root_component.get_children_components(False)
        all_component.append(root_component)


        for ism in all_component:
            count = ism.get_instance_count()
            static_mesh = ism.static_mesh
            for num in range(count):
                location = ism.get_instance_transform(num).translation
                rotation = ism.get_instance_transform(num).rotation.rotator()
                scale = ism.get_instance_transform(num).scale3d
                new_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(static_mesh, location, rotation)
                new_actor.set_actor_scale3d(scale)

        option = unreal.EditorScriptingJoinStaticMeshActorsOptions()

reverse_instance()