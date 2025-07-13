# Definition for singly-linked list.
# LeetCode already provides this
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # Step 1: Find middle
        mid = self.getMiddle(head)
        right = mid.next
        mid.next = None  # split the list
        left = head

        # Step 2: Sort both halves recursively
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def getMiddle(self, head):
        # Return middle node (first middle in case of even)
        slow = head
        fast = head.next  # ensures first middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        temp.next = list1 if list1 else list2
        return dummy.next
