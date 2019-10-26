# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# mind the case to connect either end of odd or even to None
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        cnt = 0
        first, second = head, head.next
        while head.next.next:
            tmp = head.next
            head.next = tmp.next
            head = tmp
            cnt += 1
        
        if cnt%2 == 1:
            odd_tail = head.next
            head.next = None
            odd_tail.next = second
        else:
            even_tail = head.next
            even_tail.next = None
            head.next = second
        
        return first
        