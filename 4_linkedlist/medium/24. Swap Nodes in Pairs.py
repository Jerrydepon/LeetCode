# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        second = head.next 
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second       