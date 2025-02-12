from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        self.queue.append(x)


    def pop(self):
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        
        return self.queue.popleft()


    def top(self):
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0

        

