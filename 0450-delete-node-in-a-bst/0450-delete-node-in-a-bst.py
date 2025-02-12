# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        # Search for the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            # Case 1: No child or one child (right)
            if not root.left:
                return root.right
            # Case 2: One child (left)
            elif not root.right:
                return root.left
            # Case 3: Two children
            else:
                # Find the inorder successor (smallest in the right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                
                # Copy the inorder successor's value to the current node
                root.val = successor.val
                
                # Delete the inorder successor
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
        