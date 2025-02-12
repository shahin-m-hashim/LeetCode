# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # Dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointers for traversal
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                # Bypass the current node
                prev.next = curr.next
            else:
                # Move prev forward only if no deletion
                prev = curr
            # Move curr to the next node
            curr = curr.next
        
        # Return new head (skip dummy)
        return dummy.next

        