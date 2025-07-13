# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen = set()
        
        # Traverse the first list and store all its nodes in a set
        while headA:
            seen.add(headA)
            headA = headA.next
        
        # Traverse the second list
        while headB:
            if headB in seen:
                return headB  # Intersection found
            headB = headB.next
        
        return None  # No intersection


        