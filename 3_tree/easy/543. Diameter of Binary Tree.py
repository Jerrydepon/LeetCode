# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0
        self.findMaxLength(root)
        return self.length
        
    def findMaxLength(self, root):
        if not root:
            return 0
        l = self.findMaxLength(root.left)
        r = self.findMaxLength(root.right)
        self.length = max(self.length, l+r)
        return max(l, r) + 1