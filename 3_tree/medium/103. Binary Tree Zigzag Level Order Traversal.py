# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output, queue, direction = [], collections.deque([root]), 1
        while queue:
            layer = []
            for _ in range(len(queue)):medium
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                layer.append(node.val)
            output.append(layer[::direction])
            direction *= -1
        return output
            
            