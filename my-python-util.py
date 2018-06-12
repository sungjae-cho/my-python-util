from os import listdir
from os.path import isfile, join
import os


def get_file_list(dir_path):
    if dir_path =! '/':
        dir_path = dir_path + '/'
    file_list = [ (dir_path + f) for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return file_list

def get_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension[1:]
