# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Create a map to store the parent of each node
        parent_map = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        # Step 2: Use BFS to find all nodes at distance k from the target
        result = []
        visited = set()
        queue = deque([target])
        visited.add(target)
        current_distance = 0

        # Continue BFS until the desired distance is reached
        while queue:
            if current_distance == k:
                # Collect all nodes at distance k
                result.extend(node.val for node in queue)
                return result
            for _ in range(len(queue)):
                node = queue.popleft()
                # Check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                # Check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                # Check parent
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            current_distance += 1

        return result



        