# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow_ptr, fast_ptr = head, head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next       
            fast_ptr = fast_ptr.next.next
            
            if slow_ptr == fast_ptr:     
                return True

        return False 
        


        