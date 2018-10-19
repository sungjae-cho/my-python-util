import os

def create_dir(directory):
    '''
    - Create a directory if there is no name under `directory`.
    - Nested directories can be created at once.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)
