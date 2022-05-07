# A full binary tree is a type of binary tree in which each node has either 2 children or no children

""" let, i = total no.of internal nodes
         n = total no.of nodes
         l = no.of leaf nodes
         y = no.of levels
    then,
        no.of leaves, l = i+1
        total no.of nodes, n = 2*i+1
        total no.of internal nodes, i = (n-1)/2
        no.of leaves, l = (n+1)/2
        total no.of nodes, n = 2*l-1
        no.of internal nodes, i = l-1
        no.of leaves at most = 2^(y-1)
"""

from operator import truediv


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_full_binary_tree(self, root):

        if(not root):
            return True

        if(not root.left and not root.right):
            return True

        if(root.left and root.right):
            return self.is_full_binary_tree(root.left) and self.is_full_binary_tree(root.right)

        return False


full_b_tree_obj = BinaryTreeNode(1)
print(full_b_tree_obj.is_full_binary_tree(full_b_tree_obj))
full_b_tree_obj.left = BinaryTreeNode(2)
print(full_b_tree_obj.is_full_binary_tree(full_b_tree_obj))
full_b_tree_obj.right = BinaryTreeNode(3)
print(full_b_tree_obj.is_full_binary_tree(full_b_tree_obj))
full_b_tree_obj.right.left = BinaryTreeNode(4)
print(full_b_tree_obj.is_full_binary_tree(full_b_tree_obj))
full_b_tree_obj.right = BinaryTreeNode(5)
print(full_b_tree_obj.is_full_binary_tree(full_b_tree_obj))
