# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        cur_node = head
        val = None
        while (not (cur_node is None)) and (cur_node.val != val):
            cur_node.val = val
            cur_node = cur_node.next
        if cur_node is None:
            return False
        else:
            return True
        