# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative: prev, head, cur
# recursive: similar to iterative, but with some tricks
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    # # iteratively
        # prev = None
        # while head:
        #     cur = head.next
        #     head.next = prev
        #     prev = head
        #     head = cur
        # return prev
    
    # recursively
        return self._reverse(head)
    def _reverse(self, head, prev=None):
        if not head:
            return prev     
        cur = head.next
        head.next = prev
        return self._reverse(cur, head)