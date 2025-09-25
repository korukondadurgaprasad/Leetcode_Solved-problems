# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node


class Solution:
    def insertIntoBST(self, root, val):
        # If tree is empty, new node becomes the root
        if root is None:
            return TreeNode(val)

        # If value is smaller, go to the left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # If value is larger, go to the right subtree
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        # return the root (unchanged for upper calls)
        return root
