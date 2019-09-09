# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from root, find a path with number closer to the target
# keep the difference and each value of node in a list, or return if find exactly the same value
# return the value with smalllest difference
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        li = []
        while root:
            if root.val > target:
                li.append((root.val-target, root.val))
                root = root.left
            elif root.val < target:
                li.append((target-root.val, root.val))
                root = root.right
            else:
                return root.val     
        return min(li, key=lambda x: x[0])[1]