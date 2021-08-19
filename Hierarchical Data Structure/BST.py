"""
Binary Search Tree (BST) is another tree datastructure like binary tree.
The main difference is the Node or sub-tree to the left is lesser then its parent node,
and the right sub-tree is greater.

Due to this property searching and insertion is easy.
"""

class Node:

    def __init__(self, val) -> None:
        self.left = None
        self.value = val
        self.right = None


# Search function to find a element in BST
def search(root, value):

    """
        this function returns true if ask node is present and false if it is absent,
        else it returns None
    """

    if root == None:
        return 
    
    if root.value == value: 
        return True
        
    if root.value > value:
        return search(root.left,value)
    else:
        return search(root.right,value)

    return False

# Insert function to insert a new node in BST
def insert(root, value):

    if root == None:
        return Node(value)

    if root.value == value:
        return root

    else:
        if root.value < value:
            root = insert(root.right, value)
        else:
            root = insert(root.left, value)

        
    return root


    
# Function to print the BST nodes in inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end = " ")
        inorder(root.right)


if __name__ == "__main__":

    """
    Making a simple BST

        10
        /\
       5  15
    
    """

    root = Node(10)
    root.right = Node(15)
    root.left = Node(5)

    inorder(root)
    print()
    insert(root, 3)
    insert(root, 6)
    insert(root, 2)
    
    inorder(root)
    print()
    print(search(root, 500))


"""
# Output

    5 10 15 
    5 10 15 
    None
"""





    