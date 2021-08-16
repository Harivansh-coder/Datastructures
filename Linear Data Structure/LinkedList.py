"""
A simple implementation of Linear datastructure Linkedlist.

"""

class Node:

    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        
        self.head = None
        self.tail = None

    def printll(self):

        temp = self.head

        while temp != None:
            print(temp.val, end = " ")

            temp = temp.next

        print()

    def push(self, val, flag):
        temp = Node(val)

        if flag == 0:
            temp.next = self.head
            self.head = temp
        else:
            self.tail.next = temp
            self.tail = temp
             

    def insert(self,pre ,post, node):

        pre.next = node
        node.next = post


        

if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = Node(10)

    node7 = Node(15)

    ll = LinkedList()

    ll.head = node1
    ll.tail = node5

    ll.printll()

    ll.push(0,0)
    ll.push(6,1)

    ll.insert(node2, node3, node6)
    ll.insert(node2, node6, node7)


    ll.printll()


"""
# Output

    1 2 3 4 5 
    0 1 2 15 10 3 4 5 6 
    
"""
