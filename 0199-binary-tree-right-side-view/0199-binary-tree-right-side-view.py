# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to return the Right view of the binary tree
    def rightSideView(self, root):
        res = []
        self._rightViewDFS(root, 0, res)
        return res

    # Recursive helper for right view
    def _rightViewDFS(self, node, level, res):
        if node is None:
            return

        # If we are at a new level, add the first node we see (rightmost)
        if len(res) == level:
            res.append(node.val)

        # Visit right first, then left (so rightmost appears first)
        self._rightViewDFS(node.right, level + 1, res)
        self._rightViewDFS(node.left, level + 1, res)


