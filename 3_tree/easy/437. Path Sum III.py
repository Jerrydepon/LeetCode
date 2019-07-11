# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        self.dic = {0:1}
        self.findPath(root, sum, 0)     
        return self.res
    
    def findPath(self, node, target, total):
        if not node:
            return
        total += node.val
        diff = total - target
        self.res += self.dic.get(diff, 0)
        self.dic[total] = self.dic.get(total, 0) + 1
        self.findPath(node.left, target, total)
        self.findPath(node.right, target, total)
        self.dic[total] -= 1
        
        