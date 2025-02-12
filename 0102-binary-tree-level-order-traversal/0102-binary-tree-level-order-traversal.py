from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])  # Initialize queue with root
        result = []
        
        while queue:
            level = []  # List to store nodes at the current level
            qlen = len(queue)  # Number of nodes at the current level
            
            for _ in range(qlen):
                node = queue.popleft()  # Dequeue the front node
                level.append(node.val)
                
                # Enqueue left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  # Add current level to result
        
        return result
