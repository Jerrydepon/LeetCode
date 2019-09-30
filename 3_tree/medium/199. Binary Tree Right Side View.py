# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS and choose the right node first
# append result while depth is equal to length of result list
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(res):
                    res.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        res = []
        collect(root, 0)
        return res        