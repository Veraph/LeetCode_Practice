# 155.py -- Min Stack

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
    '''
    use another queue to record the minimum val
    '''
    def __init__(self):
        self.stack, self.minStack = [], []
        self.min = float('inf')

    def push(self, x):
        self.stack.append(x)
        self.min = min(self.min, x)
        self.minStack.append(self.min)
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        self.min = float('inf') if not self.minStack else self.minStack[-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min
