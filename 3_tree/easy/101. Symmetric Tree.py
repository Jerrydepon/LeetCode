# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# outpair & inpair
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.checkSymmetry(root.left, root.right)
        
    def checkSymmetry(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val == r.val:
            outpair = self.checkSymmetry(l.left, r.right)
            inpair = self.checkSymmetry(l.right, r.left)
            return outpair and inpair
        else:
            return False