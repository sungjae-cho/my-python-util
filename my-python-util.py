from os import listdir
from os.path import isfile, join


def get_file_list(dir_path):
    if dir_path =! '/':
        dir_path = dir_path + '/'
    file_list = [ (dir_path + f) for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return file_list
