import unreal

list_assets = unreal.EditorAssetLibrary.list_assets('/Game/')

check_list = ['StaticMesh', 'Material', 'MaterialInstanceConstant',
              'Texture2D', 'ParticleSystem', 'SoundWave']

static_mesh = []
material = []
material_Instance = []
texture = []
cascade = []
sound_wave = []

lists = [static_mesh, material, material_Instance, texture, cascade, sound_wave]

def find_no_use_assets():

    for asset in list_assets:
        u_eal = unreal.EditorAssetLibrary()
        asset_data = u_eal.find_asset_data(asset)

        for num in range(len(check_list)):
            if asset_data.asset_class == check_list[num]:
                ref = u_eal.find_package_referencers_for_asset(asset)
                if not ref:
                    lists[num].append(asset)



def unreal_logging():
    unreal.log('~                                                ~')
    unreal.log('              Find Unnecessary Asset')
    unreal.log('StaticMesh, Material, Texture, Cascade, Sound Wave')
    unreal.log('~                                                ~')

    for num in range(len(check_list)):

        check_asset_name = check_list[num]
        unreal.log('================================')
        unreal.log('     ' + check_asset_name + '     ')
        unreal.log('================================')

        if lists[num]:
            for name in lists[num]:
                unreal.log(name)
        else:
            unreal.log('Nothing')

        unreal.log('---')
        unreal.log('---')

find_no_use_assets()
unreal_logging()