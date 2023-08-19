import os


def main_func(path_dir: str) -> None:
    list_name_dir = []
    print(contains_dir(path_dir, list_name_dir))


def contains_dir(path_dir: str, list_name_dir: [str] ) -> [str]:

    for i in os.listdir(path_dir):
        if os.path.isdir(path_dir+'/'+i):
            contains_dir(path_dir+'/'+i, list_name_dir)
        if os.path.isfile(path_dir+'/'+i):
            list_name_dir.append(i)
    return list_name_dir


main_func('/Users/igorkrysin/Downloads')
