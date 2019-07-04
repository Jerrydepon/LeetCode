# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        self.getHeight(root)
        return self.balanced
    
    def getHeight(self, node):
        if not node:
            return 0
        l, r = self.getHeight(node.left), self.getHeight(node.right)
        if abs(l-r) > 1:
            self.balanced = False
        return max(l, r) + 1