# 225.py -- Implement Stack using queues

'''
Only use the queue implementation
'''

class MyStack:
    '''
    use only one queue
    '''
    def __init__(self):
        self.Queue = []

    def push(self, x):
        self.Queue.append(x)
        cnt = len(self.Queue)
        while cnt > 1:
            self.Queue.append(self.Queue.pop(0))
            cnt -= 1

    def pop(self):
        return self.Queue.pop(0)

    def top(self):
        return self.Queue[0]
    
    def empty(self):
        return not self.Queue