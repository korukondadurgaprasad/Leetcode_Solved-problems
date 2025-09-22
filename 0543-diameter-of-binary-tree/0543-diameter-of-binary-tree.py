# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0   # keep diameter in an instance variable

        def height(node):
            if not node:        # empty node
                return 0
            # compute left and right heights
            left_h = height(node.left)
            right_h = height(node.right)
            # update diameter (max path between two leaves through this node)
            self.diameter = max(self.diameter, left_h + right_h)
            # return height of this subtree
            return 1 + max(left_h, right_h)

        height(root)            # compute everything
        return self.diameter
