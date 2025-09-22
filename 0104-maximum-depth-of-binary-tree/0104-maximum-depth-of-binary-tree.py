# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        # Base case: if the node is null, return 0
        if root is None:
            return 0
        # Recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # The depth of the tree is 1 current node + the maximum depth of the subtrees
        return 1 + max(left, right)
