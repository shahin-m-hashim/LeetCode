class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head  # Slow pointer
        fast = head  # Fast pointer
        
        # Move fast by 2 steps and slow by 1 step until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Slow is now at the middle node
        return slow
