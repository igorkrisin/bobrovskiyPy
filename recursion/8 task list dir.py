import os
import time


def collection_of_filenames_1(path_dir: str) -> [str]:
    result_lst = []
    for file_name in os.listdir(path_dir):
        if os.path.isdir(path_dir + '/' + file_name):
            result_lst += collection_of_filenames_1(path_dir + '/'+file_name)
        if os.path.isfile(path_dir + '/' + file_name):
            result_lst += [file_name]
    return result_lst



start = time.time()
collection_of_filenames_1('/Users/igorkrysin/Downloads')
end = time.time()
print('recurs:', (end - start))


def collection_of_filenames(path_dir: str) -> [str]:
    result_lst = []
    for file_name in os.listdir(path_dir):
        if os.path.isdir(path_dir + '/' + file_name):
            result_lst += collection_of_filenames(path_dir + '/'+file_name)
        if os.path.isfile(path_dir + '/' + file_name):
            result_lst += [file_name]
    return result_lst


start = time.time()
collection_of_filenames('/Users/igorkrysin/Downloads')
end = time.time()
print('append: ', (end - start))
