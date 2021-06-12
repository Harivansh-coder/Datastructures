"""
Queue is a popular linear data structure that uses the FIFO(first in first out) 
principle for accessing the items in the queue.
"""

class Queue:

    def __init__(self) -> None:
        self.arr = []


    #funtion return the length of the queue
    def length(self):
        return len(self.arr)

    #funtion used to insert items into the queue
    def enqueue(self,e):
        
        self.arr.append(e)
    
    #funtion remove and returns the first element inserted
    def dequeue(self):

        if (len(self.arr) == 0):
            raise "Queue is empty"
        
        return self.arr.pop(0)

    #funtion to check whether the queue is empty or not
    def is_empty(self):
        return len(self.arr) == 0

    #funtion returns the current top of the queue
    def first(self):
        if (len(self.arr) == 0):
            raise "Queue is empty"
        
        return self.arr[0]


q = Queue()

q.enqueue(5)
q.enqueue(3)
print(q.length())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())
q.enqueue(7)
q.enqueue(9)
print(q.first())
q.enqueue(4)
print(q.length())
print(q.dequeue())

print(q.dequeue())
print(q.dequeue())  #final queue[9,4]





"""
output:

2
5
False
3
True
7
3
7
9
4

"""
