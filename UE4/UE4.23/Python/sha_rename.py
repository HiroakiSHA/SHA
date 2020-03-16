import unreal
import sys

def rename_asset(search_str='', replacement_str=''):
    '''replace search_str to replacement_str

    str : search_str, replacement_str
    '''
    asset_list = unreal.EditorUtilityLibrary.get_selected_asset_data()
    for asset in asset_list:
        asset_name = asset.asset_name
        object_path = asset.object_path
        package_name = asset.package_name
        package_path = asset.package_path

        new_name = unreal.StringLibrary.replace_inline(asset_name, search_str, replacement_str)
        new_name_path = str(package_path) + '/' + new_name[1]

        #TODO : fix already an asset with same name.
        unreal.EditorAssetLibrary.rename_asset(package_name, new_name_path)


def add_prefix(prefix=''):
    asset_list = unreal.EditorUtilityLibrary.get_selected_asset_data()
    for asset in asset_list:
        asset_name = asset.asset_name
        object_path = asset.object_path
        package_name = asset.package_name
        package_path = asset.package_path

        new_name_path = str(package_path) + '/' + prefix + str(asset_name)

        #TODO : fix already an asset with same name.
        unreal.EditorAssetLibrary.rename_asset(package_name, new_name_path)


def add_suffix(suffix=''):
    asset_list = unreal.EditorUtilityLibrary.get_selected_asset_data()
    for asset in asset_list:
        asset_name = asset.asset_name
        object_path = asset.object_path
        package_name = asset.package_name
        package_path = asset.package_path

        new_name_path = str(package_path) + '/' + str(asset_name) + suffix

        #TODO : fix already an asset with same name.
        unreal.EditorAssetLibrary.rename_asset(package_name, new_name_path)

args = sys.argv

if args[1] == 'r':
    rename_asset(args[2], args[3])

if args[1] == 'p':
    add_prefix(args[2])

if args[1] == 's':
    add_suffix(args[2])