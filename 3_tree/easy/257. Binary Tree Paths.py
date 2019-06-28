# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.output = []
        self.traverseNode(root, "")
        return self.output
    
    def traverseNode(self, root, path):
        if not root.left and not root.right:
            self.output.append(path + str(root.val))
        if root.left:
            self.traverseNode(root.left, path + str(root.val) + '->')
        if root.right:
            self.traverseNode(root.right, path + str(root.val) + '->')