# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if (not head) or (not head.next):
            return False

        curr_node = head
        nodes = []
        while curr_node:
            if curr_node in nodes:
                return True
            nodes.append(curr_node)
            curr_node = curr_node.next


        