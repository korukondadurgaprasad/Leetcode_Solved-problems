# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        current = root

        while True:
            # 1. Go as left as possible
            while current:
                stack.append(current)
                current = current.left

            # 2. Pop one node — this is next smallest
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val  # kth smallest found

            # 3. Go to right subtree
            current = current.right

        