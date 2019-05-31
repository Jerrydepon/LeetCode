# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        def nextNode(node, sum):
            if not node:
                return False
            if node.val == sum and not node.left and not node.right:
                return True
        
            l = nextNode(node.left, sum-node.val)
            r = nextNode(node.right, sum-node.val)
            
            return l or r
            
        return nextNode(root, sum)