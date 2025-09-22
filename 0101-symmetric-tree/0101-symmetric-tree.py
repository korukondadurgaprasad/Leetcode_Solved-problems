# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True # An empty tree is symmetric
        return self.symmetry(root.left, root.right)

    def symmetry(self, left, right):
        if not left and not right:
            return True # Both nodes are null, so symmetric

        if not left or not right:
            return False # One of the nodes is null, so not symmetric

        if left.val != right.val:
            return False # The values of the nodes do not match, so not symmetric

        # Recursively check the children of the nodes
        return self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)
 