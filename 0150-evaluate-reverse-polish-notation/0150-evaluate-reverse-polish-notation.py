class Solution(object):
    def evalRPN(self, tokens):
        # Step 1: Create a stack
        stack = []
        
        # Step 2: Traverse each token
        for token in tokens:
            # If the token is an operator
            if token in "+-*/":
                # Pop the last two numbers from the stack
                num2 = stack.pop()
                num1 = stack.pop()
                
                # Perform the operation
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    # Important: Truncate towards zero in Python
                    result = int(float(num1) / num2)
                
                # Push the result back onto the stack
                stack.append(result)
            else:
                # It's a number, push it as an integer
                stack.append(int(token))
        
        # The result is the last element in the stack
        return stack[0]
