"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# no need to re-assign next to None
# since it is perfect binary tree, only need to check the left-most node for nodes in the level
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur  = root
        next_node = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next_node
                next_node = cur.left    
        return root