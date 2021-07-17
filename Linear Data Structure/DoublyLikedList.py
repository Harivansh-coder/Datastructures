"""
Doubly Linked List implemented in python3 
Each Node here consists of (Value, Address to next node, Address to previous node)
"""

# A linked list node of DLL
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None
 
# The push method
def push(head_ref, new_data):
 
    new_node = Node(new_data)
 
    #new_node.data = new_data
    new_node.next = head_ref
    new_node.prev = None
 
    if (head_ref != None):
        head_ref.prev = new_node
 
    head_ref = new_node
 
    return head_ref
 

 
def insertBefore(head_ref, next_node, new_data):
 
    if (next_node == None):
        print("the given next node cannot be NULL")
        return
 
    new_node = Node(new_data)
 
    new_node.prev = next_node.prev
 
    next_node.prev = new_node
 
    new_node.next = next_node
 
    if (new_node.prev != None):
        new_node.prev.next = new_node
    else:
        head_ref = new_node
 
    return head_ref
 

def printDLL(node):
    last = None
    print("Traversal in forward direction ")
    while (node != None):
        print(node.data, end=" ")
        last = node
        node = node.next
 
    print("\nTraversal in reverse direction ")
    while (last != None):
        print(last.data, end=" ")
        last = last.prev
 
 

if __name__ == '__main__':
 
    
    head = None
    head = push(head, 1)
 
    head = push(head, 2)
 
    head = push(head, 3)
 
    head = insertBefore(head, head.next, 10)
 
    print("Created DLL is: ")
    printDLL(head)
 
""""

 # Output
    Created DLL is: 
    Traversal in forward direction
    3 10 2 1
    Traversal in reverse direction
    1 2 10 3
 """