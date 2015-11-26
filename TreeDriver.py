__author__ = 'Nicholas'

import sys
from Tree import *

class TreeDriver:
    def __init__(self):
        self.tree = Tree()

def main():
    tree = Tree()
    inFile = sys.argv[1]
    tree.print_tree_levels()


if __name__ == '__main__':
    main()