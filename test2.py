"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# use a dictionary to store nodes of copied linked list
# iterate original linked list once to save the value of nodes to dictionary (key: original node, value: copied node)
# iterate original linked list again to assign next and random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur, dic = head, {}
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.arbitrary:
                dic[cur].arbitrary = dic[cur.arbitrary]
            cur = cur.next
        return dic[head]