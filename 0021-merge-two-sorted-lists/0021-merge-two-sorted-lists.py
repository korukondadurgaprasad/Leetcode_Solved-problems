class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummynode = ListNode(-1)
        temp = dummynode

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:  # ✅ Use .val instead of .data
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2

        return dummynode.next
