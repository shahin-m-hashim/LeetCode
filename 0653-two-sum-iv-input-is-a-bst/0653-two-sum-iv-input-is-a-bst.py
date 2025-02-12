# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        seen = set()
        
        # DFS Function for Tree Traversal
        def dfs(node):
            if not node:
                return False
            
            # Check for the complement in the HashSet
            if k - node.val in seen:
                return True
            
            # Add the current node's value to the HashSet
            seen.add(node.val)
            
            # Continue to search in left and right subtrees
            return dfs(node.left) or dfs(node.right)
        
        # Start DFS from the root
        return dfs(root)
        