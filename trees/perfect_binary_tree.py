"""
A perfect binary tree is a special type of binary tree in which each internal node must have either 0 or 2 children.
It's same as full binary tree until now.
A perfect binary tree also need to have all the leaf nodes on same level. This is the only difference between a full and
perfect binary tree.
All perfect binary trees are full binary trees in this sense.

A perfect binary tree of height h has 2^(h + 1) - 1 node.
A perfect binary tree with n nodes has height log(n + 1) - 1 = Θ(ln(n)).
A perfect binary tree of height h has 2^h leaf nodes.
The average depth of a node in a perfect binary tree is Θ(ln(n)).

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_of_node(node):
    d = 0
    while(node):
        d += 1
        node = node.left
    return d


def is_perfect_binary_tree(root, d, level):
    if(not root):
        return True

    if(not root.left and not root.right):
        return (d == level+1)

    if(not root.left or not root.right):
        return False

    return (is_perfect_binary_tree(root.left, d, level + 1) and is_perfect_binary_tree(root.right, d, level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

print(is_perfect_binary_tree(root, depth_of_node(root), 0))
