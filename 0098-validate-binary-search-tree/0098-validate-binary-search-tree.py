# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        # Helper function to validate the BST
        def validate(node, min_val, max_val):
            # Base case: if the node is None, return True
            if not node:
                return True
            
            # Check if the node's value falls within the valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate the left subtree
            # Update the max value to the current node's value
            left_is_valid = validate(node.left, min_val, node.val)
            
            # Recursively validate the right subtree
            # Update the min value to the current node's value
            right_is_valid = validate(node.right, node.val, max_val)
            
            # Both subtrees must be valid for the tree to be a BST
            return left_is_valid and right_is_valid
        
        # Initial call with the full range of values
        return validate(root, float('-inf'), float('inf'))

