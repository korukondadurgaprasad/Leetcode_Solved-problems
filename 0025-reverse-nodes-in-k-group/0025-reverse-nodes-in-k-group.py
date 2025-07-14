# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        def reverseLinkedList(head):
            temp = head
            prev = None
            while temp is not None:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev

        def getKthNode(temp, k):
            k -= 1
            while temp is not None and k > 0:
                k -= 1
                temp = temp.next
            return temp

        temp = head
        prevLast = None

        while temp is not None:
            kThNode = getKthNode(temp, k)
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kThNode.next
            kThNode.next = None

            reversedHead = reverseLinkedList(temp)

            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode

            prevLast = temp
            temp = nextNode

        return head
