"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# use stack to deal with child first
# remember to set node.next = None & node.child = None
# usage of pointer pre
# link to None in the end (because need dummy to get the head)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        dummy = Node(0, None, head, None)     
        pre = dummy
        stack = [head]
        while stack:
            node = stack.pop()

            node.prev = pre
            pre.next = node
            
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            pre = node        
            
        
        dummy.next.prev = None
        return dummy.next        