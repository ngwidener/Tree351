__author__ = 'Nicholas'

import sys
from Tree import *

class TreeDriver:
    def __init__(self):
        self.tree = Tree()

def main():
    tree = Tree()
    inFile = sys.argv[1]
    prnt = tree.read_paths(inFile)
    #print(prnt)
    tree.do_stuff(inFile)



if __name__ == '__main__':
    main()