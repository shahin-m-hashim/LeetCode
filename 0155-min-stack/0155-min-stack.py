class MinStack(object):

    def __init__(self):
        # Step 1: Initialize two stacks
        self.stack = []      # Main stack to store all elements
        self.minStack = []   # Min stack to store minimums

    def push(self, val):
        """
        Push element onto stack.
        If val is less than or equal to current minimum, push it to minStack.
        """
        self.stack.append(val)
        
        # If minStack is empty or val is the new minimum, push to minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        """
        Pop the top element from stack.
        If it is the current minimum, pop from minStack as well.
        """
        if self.stack:
            top = self.stack.pop()
            # If the popped value is the current minimum, pop from minStack
            if top == self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        """
        Return the top element of the stack.
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        """
        return self.minStack[-1] if self.minStack else None
