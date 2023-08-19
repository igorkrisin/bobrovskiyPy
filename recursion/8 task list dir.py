import os


def main_func(path_dir: str) -> None:
    list_name_file = []
    print(collection_of_filenames(path_dir, list_name_file))


def collection_of_filenames(path_dir: str, list_name_file: [str]) -> [str]:

    for file_name in os.listdir(path_dir):
        if os.path.isdir(path_dir+'/'+file_name):
            collection_of_filenames(path_dir+'/'+file_name, list_name_file)
        if os.path.isfile(path_dir+'/'+file_name):
            list_name_file.append(file_name)
    return list_name_file


main_func('/Users/igorkrysin/Downloads')
