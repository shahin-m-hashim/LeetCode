class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        # Queue to perform BFS, storing (node, depth)
        queue = [(root, 1)]
        
        while queue:
            node, depth = queue.pop(0)
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add children to queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
