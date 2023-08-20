import os


def collection_of_filenames(path_dir: str) -> [str]:
    result_lst = []
    for file_name in os.listdir(path_dir):
        if os.path.isdir(path_dir + '/' + file_name):
            result_lst = collection_of_filenames(path_dir + '/'+file_name) + result_lst
        if os.path.isfile(path_dir + '/' + file_name):
            result_lst += [file_name]
    return result_lst


print(collection_of_filenames('/Users/igorkrysin/Downloads'))

