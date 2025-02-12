class Solution(object):
    def isValid(self, s):
        # Step 1: Create a stack
        stack = []
        
        # Step 2: Mapping of closing brackets to opening brackets
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Step 3: Traverse each character
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Check the top of the stack
                top = stack.pop() if stack else '#'
                
                # If the top doesn't match the corresponding opening bracket
                if mapping[char] != top:
                    return False
            else:
                # It's an opening bracket, push it to the stack
                stack.append(char)
        
        # Step 4: Check if the stack is empty at the end
        return not stack
