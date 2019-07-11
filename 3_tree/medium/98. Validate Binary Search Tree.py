# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.traverseTree(root, -float("inf"), float("inf"))
    
    def traverseTree(self, node, l_range, r_range):
        if not node:
            return True  
        if not(l_range < node.val < r_range):
            return False
        l = self.traverseTree(node.left, l_range, min(r_range, node.val))
        r = self.traverseTree(node.right, max(l_range, node.val), r_range)
        return l and r