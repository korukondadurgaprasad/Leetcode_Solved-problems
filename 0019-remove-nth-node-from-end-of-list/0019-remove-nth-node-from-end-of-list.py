# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        slow=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        delnode=slow.next
        slow.next=slow.next.next
        delnode=None
        return head