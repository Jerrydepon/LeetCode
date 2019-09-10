# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# fast pointer moves two steps and slow pointer moves one step per loop
# no loop if fast meets the Null end
# find loop if fast meets with slow
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        fast, slow = head, head
        while fast.next:
            fast = fast.next.next
            if not fast:
                return False
            slow = slow.next
            
            if fast is slow:
                return True
        return False        