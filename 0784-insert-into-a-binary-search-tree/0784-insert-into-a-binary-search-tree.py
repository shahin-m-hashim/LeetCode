# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
       # If root is None, place the new value here
        if not root:
            return TreeNode(val)
        
        # Traverse the tree to find the correct spot
        if val > root.val:
            # Go to the right subtree
            root.right = self.insertIntoBST(root.right, val)
            
        else:
            # Go to the left subtree
            root.left = self.insertIntoBST(root.left, val)
            
        
        # Return the root as it remains unchanged
        return root
        