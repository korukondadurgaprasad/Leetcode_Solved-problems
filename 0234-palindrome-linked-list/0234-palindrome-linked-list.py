# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node = self.reverse_ll(slow.next)
        first = head
        second = new_node
        while second:
            if first.val != second.val:
                self.reverse_ll(new_node)
                return False
            first = first.next
            second = second.next

        self.reverse_ll(new_node)
        return True

    def reverse_ll(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

