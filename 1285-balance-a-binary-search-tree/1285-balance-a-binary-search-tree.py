# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        # Step 1: In-order traversal to get sorted node values
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Construct balanced BST from sorted values
        def build_balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nodes[mid])
            root.left = build_balanced_bst(left, mid - 1)
            root.right = build_balanced_bst(mid + 1, right)
            return root
        
        # Step 3: Build and return the new balanced tree
        return build_balanced_bst(0, len(nodes) - 1)
        