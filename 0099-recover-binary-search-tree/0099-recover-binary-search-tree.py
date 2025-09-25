# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        self.first = self.middle = self.last = self.prev = None

        def inorder(node):
            if not node:
                return
            
            # Go to left subtree
            inorder(node.left)

            # Check if current node is smaller than previous node
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    # First violation
                    self.first = self.prev
                    self.middle = node
                else:
                    # Second violation
                    self.last = node
            
            # Update prev to current node
            self.prev = node

            # Go to right subtree
            inorder(node.right)

        # Start inorder traversal
        inorder(root)

        # Swap nodes to fix the BST
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
