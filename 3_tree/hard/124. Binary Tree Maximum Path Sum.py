# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# find the maximum path for each node (node + left or right)
# each node represents a maximum sum of node and one of its path
# search for a node with maximum sum of node, left, and right 
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float('inf')
        dumb = self.findPathSum(root)
        return self.max_sum
        
    def findPathSum(self, node):
        if not node:
            return 0
        
        left = self.findPathSum(node.left)
        right = self.findPathSum(node.right)
        
        left, right = max(left, 0), max(right, 0)

        self.max_sum = max(self.max_sum, node.val+left+right)
        return node.val + max(left, right)

