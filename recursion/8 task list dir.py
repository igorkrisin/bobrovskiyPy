import os

# print(os.getcwd())

os.chdir('/Users/igorkrysin/Documents/dev/bobrovskiy')


# print(os.getcwd())
# print(os.listdir('/Users/igorkrysin/Documents/dev/bobrovskiy'))


def contains_dir(name_dir: str) -> None:
    list_dir_plus_file = []
    result_list = []
    list_dir_plus_file = os.listdir(name_dir)
    print(list_dir_plus_file)

    for path in os.listdir(name_dir):
        if os.path.isfile(os.path.join(name_dir, path)):
            result_list.append(path)
        elif not os.path.isfile(os.path.join(name_dir, path)):
            result_list.append(contains_dir(os.path.join(name_dir, path)))
    print(result_list)


contains_dir('/Users/igorkrysin/Documents')
