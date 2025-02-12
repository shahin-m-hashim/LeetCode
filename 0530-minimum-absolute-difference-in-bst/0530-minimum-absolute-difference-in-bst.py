# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        stack = []
        prev = None
        min_diff = float('inf')
        
        # In-order traversal using stack
        while stack or root:
            # Go as left as possible
            while root:
                stack.append(root)
                root = root.left
            
            # Process the current node
            root = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, abs(root.val - prev))
            # Update previous value
            prev = root.val
            
            # Move to the right subtree
            root = root.right
        
        return min_diff