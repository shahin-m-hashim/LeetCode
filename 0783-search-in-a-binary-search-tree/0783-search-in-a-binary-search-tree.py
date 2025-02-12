# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        # Base case: if root is None or the root's value is the target value
        if not root or root.val == val:
            return root
        
        # If target value is less, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If target value is greater, search in the right subtree
        return self.searchBST(root.right, val)
        