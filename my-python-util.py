from os import listdir
from os.path import isfile, join


def get_file_list(dir_path):
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return onlyfiles
