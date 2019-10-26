# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# in-order DFS
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.li = []
        self.searchTree(root)
        return self.li[k-1]
        
    def searchTree(self, node):
        if not node:
            return
        self.searchTree(node.left)
        self.li.append(node.val)
        self.searchTree(node.right)