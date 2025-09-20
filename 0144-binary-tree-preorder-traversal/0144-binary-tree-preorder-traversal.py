# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution(object):
    def _preorder(self, node, ans):
        """helper function for preorder traversal"""
        if node is None:
            return
        ans.append(node.val)          # visit root
        self._preorder(node.left, ans)  # go left
        self._preorder(node.right, ans) # go right

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        self._preorder(root, ans)  # get full preorder traversal list
        # return only the 2nd and 3rd values (index 1 and 2)
        return ans            # if list shorter, it just returns whatever available
