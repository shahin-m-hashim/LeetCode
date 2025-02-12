class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow = head  # Slow pointer
        fast = head  # Fast pointer
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps
            
            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, there is no cycle
        return False
