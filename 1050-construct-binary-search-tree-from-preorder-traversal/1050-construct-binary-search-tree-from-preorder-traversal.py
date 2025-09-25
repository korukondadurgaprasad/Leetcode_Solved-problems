# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder):
        return self._bstFromPreorderHelper(preorder, float('inf'), [0])

    def _bstFromPreorderHelper(self, preorder, bound, index):
        if index[0] == len(preorder) or preorder[index[0]] > bound:
            return None

        root = TreeNode(preorder[index[0]])
        index[0] += 1

        root.left = self._bstFromPreorderHelper(preorder, root.val, index)
        root.right = self._bstFromPreorderHelper(preorder, bound, index)

        return root
