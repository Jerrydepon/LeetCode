# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# (use of dummy)
# iterate through the list and ignore the target value node
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next        
        
        
#         if not head:
#             return None
        
#         prev = None
#         cur = head
#         while cur:
#             if cur.val == val and not prev:
#                 head = cur.next
#             elif cur.val == val:
#                 prev.next = cur.next
#             else:
#                 prev = cur
#             cur = cur.next
#         return head
            