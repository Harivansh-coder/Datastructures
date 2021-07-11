"""Binary Tree implemented in python3"""

class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.left = None
        self.right = None

def inOrder(root):
    if root:

        inOrder(root.left)

        print(root.val, end = " ")

        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)

        postOrder(root.right)

        print(root.val,end = " ")


def preOrder(root):
    if root: 
        print(root.val, end=" ")

        preOrder(root.left)

        preOrder(root.right)

if __name__ == '__main__':
    
    root = Node(5)

    root.left = Node(4)

    root.right = Node(6)

    root.left.left = Node(3)

    root.left.right = Node(10)

    
    inOrder(root)
    print("Inorder")

    
    preOrder(root)
    print("Preorder")

   
    postOrder(root)
    print("Postorder")


"""
# OUTPUT

    3 4 10 5 6 Inorder
    5 4 3 10 6 Preorder
    3 10 4 6 5 Postorder
"""

