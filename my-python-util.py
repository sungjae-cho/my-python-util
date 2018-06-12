from os import listdir
from os.path import isfile, join
import os


def get_file_list(dir_path, extension=''):
    file_list = list()
    for f in listdir(dir_path):
        if isfile(join(dir_path, f)):
            file_path = dir_path + f
            if extension == '':
                file_list.append(file_path)
            else:
                if get_extension(file_path) == extension:
                    file_list.append(file_path)
    return file_list

def get_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension[1:]

def get_file_name(file_path):
    file_name, _ = os.path.splitext(file_path)
    return file_name
