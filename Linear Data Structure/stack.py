"""
Stack is a popular linear data structure that uses the LIFO(last in first out) 
principle for accessing the items in the stack.
"""

class Stack:

    def __init__(self) -> None:
        self.arr = []

    #funtion return the length of the stack
    def length(self):
        return len(self.arr)

    #funtion used to push(insert) items into the stack
    def push(self,e):
        
        self.arr.append(e)
    
    #funtion remove and returns the last element inserted
    def pop(self):

        if (len(self.arr) == 0):
            raise "stack is empty"
        
        return self.arr.pop()

    #funtion to check whether the stack is empty or not
    def is_empty(self):
        return len(self.arr) == 0

    #funtion returns the current top of the stack
    def top(self):
        if (len(self.arr) == 0):
            raise "stack is empty"
        
        return self.arr[-1]


sc = Stack()

sc.push(5)
sc.push(3)
print(sc.length())
print(sc.pop())
print(sc.is_empty())
print(sc.pop())
print(sc.is_empty())
sc.push(7)
sc.push(9)
print(sc.top())
sc.push(4)
print(sc.length())
print(sc.pop())
sc.push(6)  
#[7, 6, 9] the final stack

"""
output:

2
3    
False
5    
True 
9
3
4

"""




