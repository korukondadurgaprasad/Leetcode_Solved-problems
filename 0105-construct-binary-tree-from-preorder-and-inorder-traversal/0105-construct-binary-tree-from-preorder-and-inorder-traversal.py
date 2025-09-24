# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # The first element of preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the position of root in inorder
        mid = inorder.index(root_val)

        # Build left and right subtrees using slicing
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
