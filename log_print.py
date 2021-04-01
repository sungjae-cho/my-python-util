'''
This implemenation is inhereted from https://stackoverflow.com/a/14906787 .
PrintLogger takes printed text at the standard output and saves it to log_path.
This allows both standard output display and logging on a file.
'''

import sys

class PrintLogger(object):
    def __init__(self, log_path):
        self.terminal = sys.stdout
        self.log = open(log_path, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

# Set sys.stdout as an instance of PrintLogger
sys.stdout = PrintLogger()
