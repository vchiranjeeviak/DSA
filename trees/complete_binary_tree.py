"""
A complete binary tree is a type of binary tree in which
all internal nodes have 2 children except for the last internal node
The last internal node can have one child and that child should be the left one and not the right one
"""


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def no_of_nodes(root):
    if(not root):  # If there is no node there, return 0
        return 0

    return (1 + no_of_nodes(root.left) + no_of_nodes(root.right))
    # Else count the present node and recurse through left and right subtrees


def is_complete_binary_tree(root, index, nodes):
    if (not root):  # If tree is empty, return true
        return True
    if (index >= nodes):  # If index of current node is greater than or equal to total no.of nodes, return false
        return False
    # ELse check left and right subtrees
    return (is_complete_binary_tree(root.left, 2*index + 1, nodes) and is_complete_binary_tree(root.right, 2*index+2, nodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(is_complete_binary_tree(root, 0, no_of_nodes(root)))
