class Node:  # Every node in a tree has a value, a left subtree and a right subtree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if(root):
            self.inorder(root.left)
            print(str(root.val)+"->", end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if(root):
            print(str(root.val)+"->", end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.val)+"->", end=" ")


tree_obj = Tree()
tree_obj.root = Node(1)
tree_obj.root.left = Node(2)
tree_obj.root.right = Node(3)
tree_obj.root.left.left = Node(4)
tree_obj.root.left.right = Node(5)
print('Inorder')
tree_obj.inorder(tree_obj.root)
print()
print('Preorder')
tree_obj.preorder(tree_obj.root)
print()
print('Postorder')
tree_obj.postorder(tree_obj.root)
print()
