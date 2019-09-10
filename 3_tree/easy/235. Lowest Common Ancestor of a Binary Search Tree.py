# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# loop until node is between p and q, or node equal to either p or q
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
#         # method of Q.236
#         if not root:
#             return None
#         if root == p or root == q:
#             return root
        
#         left = self.lowestCommonAncestor(root.left, p , q)
#         right = self.lowestCommonAncestor(root.right, p, q)
        
#         if left and right:
#             return root
#         if not left:
#             return right
#         if not right:
#             return left