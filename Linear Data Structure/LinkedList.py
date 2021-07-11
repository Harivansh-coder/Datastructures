class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.next = None

    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # Tranverse through the Linked List and print values
    def printll(self):
    
        temp = self.head
        while temp:
            print(temp.val,end = " ")
            temp = temp.next

    # insert the element at the start of the list
    def push(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp 


    def insert(self,val,preNode):
        temp = Node(val)

        temp.next = preNode.next
        preNode.next = temp


            

if __name__== '__main__':
    
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.push(5)

    ll.push(10)

    ll.push(11)

    ll.push(15)

    ll.insert(12,third)

    ll.push(0)

    ll.push(12)

    ll.printll()
    
    
"""
#   OUTPUT

    12 0 15 11 10 5 1 2 3 12 
    
"""
