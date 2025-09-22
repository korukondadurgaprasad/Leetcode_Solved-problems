# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMaxPathSum(self, root, maxi):
        # Base case: If the current node is null, return 0
        if not root:
            return 0

        # Calculate the maximum path sum
        # for the left and right subtrees
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))

        # Update the overall maximum
        # path sum including the current node
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)

        # Return the maximum sum considering
        # only one branch (either left or right)
        # along with the current node
        return max(leftMaxPath, rightMaxPath) + root.val

    def maxPathSum(self, root):
        # Initialize maxi to the
        # minimum possible integer value
        maxi = [float('-inf')]

        # Call the recursive function to
        # find the maximum path sum
        self.findMaxPathSum(root, maxi)

        # Return the final maximum path sum
        return maxi[0]

