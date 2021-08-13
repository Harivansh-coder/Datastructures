"""
Implementation of binary tree.
Traversal of the binary tree.
Insertion in binary tree.
"""

class Node:

    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.value = key

def traversal(root):

    if root == None:
        return
    
    traversal(root.left)
    print(root.value,end = " ")
    traversal(root.right)


def insert(node, val):

    temp = node
    while (True):
        
 
        if (temp.left == None):
            temp.left = Node(val)
            break
        else:
            temp = temp.left
 
        if (temp.right == None):
            temp.right = Node(val)
            break
        else:
            temp = temp.right


    



if __name__ == "__main__":

    root = Node(50)

    root.left = Node(30)
    root.right = Node(100)

    root.left.left = Node(20)
    

    root.right.left = Node(25)
    root.right.right = Node(120)

    traversal(root)

    insert(root, 100)

    print()
    traversal(root)





"""
# Output:

    20 30 50 25 100 120  // before insertion of 100
    20 30 100 50 25 100 120 // after insertion of 100
"""

    
