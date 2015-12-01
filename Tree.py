__author__ = 'Nicholas Widener'
__author__ = 'Trent Weatherman'


import sys
from PathNode import PathNode

class Tree():


    def __init__(self):
        self.path_list = []
        self.root = None
        self.last_node = None

    def read_paths(self, input_file):
        with open(input_file, "r") as paths:
            for line in paths:
                self.path_list.append(line.rstrip())
        return self.path_list

    def build_complete_tree(self):
        if (len(self.path_list) != 1):
            self.populate_tree()
            self.set_sibling_links(self.root)

    def populate_tree(self, index=1, new_parent=None):
        current_node = PathNode(self.path_list[index])
        if (index == 1):
            self.root = current_node

        if (index == len(self.path_list) - 1):
            self.last_node = current_node
        current_node.set_parent(new_parent)

        if (index*2+1 < len(self.path_list)):
            current_node.set_left_child(self.populate_tree(index*2+1, current_node))
        if (index*2+2 < len(self.path_list)):
            current_node.set_right_child(self.populate_tree(index*2+2, current_node))

        return current_node

    def set_sibling_links(self, root):
        '''
        Sets the sibling links for every PathNode in the tree.

        @param root: The root of the binary tree or a subtree.
        '''
        if (root == self.root and root.left_child != None and root.left_child != self.last_node):
            root.left_child.sibling = root.right_child
            self.set_sibling_links(root.left_child)
            self.set_sibling_links(root.right_child)
        else:
            if (root.left_child != None and root.left_child != self.last_node):
                root.left_child.sibling = root.right_child
                if (root.sibling != None):
                    root.right_child.sibling = root.sibling.left_child
                self.set_sibling_links(root.left_child)
                self.set_sibling_links(root.right_child)


    def print_tree_levels(self):
        '''
        Prints the lengths of the paths in each level of the tree.
        '''
        #source_dest = self.read_source_dest(sys.argv[2])
        #print('[' + str(source_dest[0]) + ', ' + str(source_dest[1]) + ']')
        if (len(self.path_list) != 1):
            print('\tRoot: ' + str(len(self.root.path) - 1))
            end_node = self.root.left_child
            current_level = 1
            while end_node != None:
                string = '\tLevel ' + str(current_level) + ': '
                current_node = end_node
                while current_node != None:
                    #print("is it printing here")
                    string += str(len(current_node.path) - 1) + ' '
                    current_node = current_node.sibling
                print(string)
                current_level += 1
                end_node = end_node.left_child


    def do_stuff(self, in_file):
        self.read_paths(in_file)
        self.build_complete_tree()
        self.print_tree_levels()
