# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None         # Previous node starts as None
        curr = head         # Current node starts at head
        
        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev to current node
            curr = next_node       # Move to the next node
        
        return prev  # New head of the reversed list
        