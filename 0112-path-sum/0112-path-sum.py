class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        # If root is None, return False as there's no path
        if not root:
            return False
        
        # Stack will store (current_node, current_sum)
        stack = [(root, root.val)]
        
        # Iterate while there are nodes to process
        while stack:
            node, current_sum = stack.pop()
            
            # If it's a leaf node, check if the path sum matches targetSum
            if not node.left and not node.right:
                if current_sum == targetSum:
                    return True
            
            # Push right child to stack if it exists
            if node.right:
                stack.append((node.right, current_sum + node.right.val))
            
            # Push left child to stack if it exists
            if node.left:
                stack.append((node.left, current_sum + node.left.val))
        
        # If no path matches targetSum, return False
        return False
