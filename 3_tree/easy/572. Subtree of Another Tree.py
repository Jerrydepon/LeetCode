# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        subtree = False
        if s.val == t.val:
            subtree = self.checkSubtree(s, t)
        return subtree or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
            
    def checkSubtree(self, s, t):
        if not (s and t):
            return s == t
        return s.val == t.val and self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)
        
        # # redundant way
        # l = r = True
        # if not s and not t:
        #     return True
        # if s.val != t.val:
        #     return False
        # if (s.left and not t.left) or (not s.left and t.left) or (s.right and not t.right) or (not s.right and t.right):
        #     return False
        # if s.left:
        #     l = self.checkSubtree(s.left, t.left) 
        # if s.right:
        #     r = self.checkSubtree(s.right, t.right)
        # return l and r
            