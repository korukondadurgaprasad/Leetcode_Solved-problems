# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        # Traverse the tree until we find the node 
        # with the given value or reach the end
        while root is not None and root.val != val:
            # Move to the left or right child 
           # depending on the value comparison
            root = root.left if root.val > val else root.right
        # Return the found node or None if not found
        return root 