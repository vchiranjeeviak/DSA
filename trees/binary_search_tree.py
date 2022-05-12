from requests import delete


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if(not root):
            return

        self.inorder(root.left)
        print(str(root.val)+"->", end=" ")
        self.inorder(root.right)
        return

    def insert(self, root, val):
        if(not root):
            root = Node(val)
            return root

        if(val < root.val):
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def minNode(self, root):
        while(not root.left):
            root = root.left
        return root

    def delete(self, root, val):
        if(not root):
            return root

        if (val < root.val):
            root.left = self.delete(root.left, val)
        elif (val > root.val):
            root.right = self.delete(root.right, val)
        else:
            if (not root.left):
                temp = root.right
                root = None
                return temp
            elif (not root.right):
                temp = root.left
                root = None
                return temp

            temp = self.minNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        return root


tree = BST()
tree.root = tree.insert(tree.root, 4)
tree.root = tree.insert(tree.root, 3)
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 1)
tree.root = tree.insert(tree.root, 7)
tree.root = tree.insert(tree.root, 6)
tree.inorder(tree.root)
print()
tree.root = tree.delete(tree.root, 5)
tree.inorder(tree.root)
print()
