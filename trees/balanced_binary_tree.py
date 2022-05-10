class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


def is_balanced(root, height):

    left_height = Height()
    right_height = Height()

    if(not root):
        return True

    l = is_balanced(root.left, left_height)
    r = is_balanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if(abs(left_height.height - right_height.height) <= 1):
        return True

    return False


height = Height()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)

print(is_balanced(root, height))
