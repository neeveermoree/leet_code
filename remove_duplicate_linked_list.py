# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            previous = ListNode(head.val, None)
            answer = previous
        else:
            return None
        while head:
            if head.val > previous.val:
                previous.next = ListNode(head.val, None)
                previous = previous.next
            head = head.next
        return answer
