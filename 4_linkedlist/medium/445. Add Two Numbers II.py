# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use two stacks to reverse the node in linked lists
# assign a new node as head and link to the previous node 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = ListNode(0)
        while s1 or s2:
            val = 0
            if s1:
                val += s1.pop()
            if s2:
                val += s2.pop()
            carry, val = divmod(carry + val, 10)
            
            head.val = val
            temp = head
            head = ListNode(0)
            head.next = temp 
            
        if carry: 
            head.val = carry
             
        return head if head.val else head.next 