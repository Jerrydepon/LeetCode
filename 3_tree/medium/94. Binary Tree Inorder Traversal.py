# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# basic in-order DFS
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.searchTree(root)
        return self.res
        
    def searchTree(self, node):
        if not node:
            return
        self.searchTree(node.left)
        self.res.append(node.val)
        self.searchTree(node.right)