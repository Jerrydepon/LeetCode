# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from leaves and count each node's depth by max depth of left or right node plus 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def maxSubDepth(node):
            if not node:
                return 0
            l = maxSubDepth(node.left) + 1
            r = maxSubDepth(node.right) + 1
            return max(l, r)
        
        return maxSubDepth(root)