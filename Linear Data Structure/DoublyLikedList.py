# A complete working Python program to demonstrate all
# insertion before a given node
 
# A linked list node
class Node:
    def __init__(self, x):
        self.data = x
        self.prev = None
        self.next = None
 

def push(head_ref, new_data):
 
    # /* 1. allocate node */
    new_node = Node(new_data)
 
    # /* 2. put in the data */
    new_node.data = new_data
 
    # /* 3. Make next of new node as
    # head and previous as None */
    new_node.next = head_ref
    new_node.prev = None
 
    # /* 4. change prev of head node to new node */
    if (head_ref != None):
        head_ref.prev = new_node
 
    # /* 5. move the head to point to the new node */
    head_ref = new_node
 
    return head_ref
 

 
def insertBefore(head_ref, next_node, new_data):
 
    # /*1. check if the given next_node is NULL */
    if (next_node == None):
        print("the given next node cannot be NULL")
        return
 
    # /* 3. put in the data */
    new_node = Node(new_data)
 
    # /* 4. Make prev of new node as prev of next_node */
    new_node.prev = next_node.prev
 
    # /* 5. Make the prev of next_node as new_node */
    next_node.prev = new_node
 
    # /* 6. Make next_node as next of new_node */
    new_node.next = next_node
 
    # /* 7. Change next of new_node's previous node */
    if (new_node.prev != None):
        new_node.prev.next = new_node
 
    # /* 8. If the prev of new_node is NULL, it will be
    #   the new head node */
    else:
        head_ref = new_node
 
    return head_ref
 

def printList(node):
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
    head = push(head, 7)
 
    head = push(head, 1)
 
    head = push(head, 4)
 
    head = insertBefore(head, head.next, 8)
 
    print("Created DLL is: ")
    printList(head)
 