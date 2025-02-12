class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        # Base case: if the root is None, no path exists
        if not root:
            return False
        
        # If we're at a leaf node, check if the path sum equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees with the updated sum
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
