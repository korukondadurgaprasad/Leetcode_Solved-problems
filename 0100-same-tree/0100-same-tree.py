# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        # If both nodes are null, the trees are the same
        if not p and not q:
            return True

        # If one of the nodes is null, the trees are not the same
        if not p or not q:
            return False

        # If the values of the nodes are different, the trees are not the same
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)