# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 1: Reach node before the 'left' position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist
        # 'start' is the first node in the sublist to be reversed
        start = prev.next
        then = start.next
        
        # Reverse nodes between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        # Return the modified list
        return dummy.next

        