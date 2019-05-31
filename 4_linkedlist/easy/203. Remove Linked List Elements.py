# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        prev = None
        cur = head
        while cur:
            if cur.val == val and not prev:
                head = cur.next
            elif cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
            