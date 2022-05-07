class BinaryTreeNode:  # A binary tree is a tree in which every node can have atmost 2 children
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder(self):
        if(self.left):
            self.left.inorder()
        print(str(self.val)+"->", end=" ")
        if(self.right):
            self.right.inorder()

    def preorder(self):
        print(str(self.val)+"->", end=" ")
        if(self.left):
            self.left.preorder()
        if(self.right):
            self.right.preorder()

    def postorder(self):
        if(self.left):
            self.left.postorder()
        if(self.right):
            self.right.postorder()
        print(str(self.val)+"->", end=" ")


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(5)
print('Inorder traversal:')
root.inorder()
print()
print('Preorder traversal:')
root.preorder()
print()
print('Postorder traversal:')
root.postorder()
print()
