# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Helper function to connect subtrees after deleting a node
    def connector(self, root):
        # Case 1: no left child
        if not root.left:
            return root.right

        # Case 2: no right child
        if not root.right:
            return root.left

        # Case 3: both children exist
        # find the leftmost node in the right subtree
        leftmost = root.right
        while leftmost.left:
            leftmost = leftmost.left

        # attach the left subtree to that node
        leftmost.left = root.left

        # return the right subtree as the new root
        return root.right

    # Function to delete a node with a specific key from the binary search tree.
    def deleteNode(self, root, key):
        if root is None:
            return None

        # if the node to delete is the root itself
        if root.val == key:
            return self.connector(root)

        node = root
        while node:
            if node.val > key:
                if node.left and node.left.val == key:
                    node.left = self.connector(node.left)
                    break
                else:
                    node = node.left
            else:
                if node.right and node.right.val == key:
                    node.right = self.connector(node.right)
                    break
                else:
                    node = node.right
        return root
