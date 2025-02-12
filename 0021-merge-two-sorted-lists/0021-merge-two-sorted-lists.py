# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Step 1: Dummy node and pointer to build the merged list
        dummy = ListNode()  # Dummy node to start the merged list
        tail = dummy
        
        # Step 2: Compare and merge nodes from both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Step 3: Attach remaining nodes from either list1 or list2
        tail.next = list1 if list1 else list2
        
        # Step 4: Return the merged list, starting from the node after the dummy
        return dummy.next
        