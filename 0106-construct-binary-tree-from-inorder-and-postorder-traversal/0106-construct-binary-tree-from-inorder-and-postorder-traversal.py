# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # Last element of postorder is the root value
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find root value in inorder
        idx = inorder.index(root_val)

        # Build right subtree first (because postorder ends with root)
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])

        return root


        