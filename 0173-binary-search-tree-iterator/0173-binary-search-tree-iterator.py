# Definition for a binary tree node.


class BSTIterator:

    def __init__(self, root):
        # Initialize the iterator on the root of the BST      
        self.stack = []
        self._pushAll(root)

    def hasNext(self):
        # Returns true if there is a next element in the iterator     
        return len(self.stack) > 0

    def next(self):
        # Returns the next smallest element in the BST
        temp = self.stack.pop()
        self._pushAll(temp.right)
        return temp.val

    def _pushAll(self, node):
        # Helper function to push all the left nodes onto the stack
        # type node: TreeNode
       
        while node is not None:
            self.stack.append(node)
            node = node.left

