# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# since l1 and l2 are already in reversed order
# iterate through both lists step by step and keep track of carry
# add a node to new linked list if there is node in either l1, l2, or carry
# use dummy to return the head of new list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        dummy, carry = l3, 0
        while l1 or l2 or carry:
            sum_ = 0
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            if carry:
                sum_ += carry
                
            l3.next = ListNode(sum_%10)
            carry = sum_ // 10
            l3 = l3.next
        return dummy.next
            
        
#         # redundant        
#         l3 = ListNode(0)
#         head, carry = l3, 0
#         while l1 and l2:
#             sum_ = l1.val + l2.val + carry
#             digit = sum_ % 10
#             carry = sum_ // 10
#             l3.next = ListNode(digit)
#             l1, l2, l3 = l1.next, l2.next, l3.next
        
#         if l1:
#             while l1:
#                 sum_ = l1.val + carry
#                 digit = sum_ % 10
#                 carry = sum_ // 10
#                 l3.next = ListNode(digit) 
#                 l1, l3 = l1.next, l3.next
#         elif l2:
#             while l2:
#                 sum_ = l2.val + carry
#                 digit = sum_ % 10
#                 carry = sum_ // 10
#                 l3.next = ListNode(digit) 
#                 l2, l3 = l2.next, l3.next
#         if carry:
#             l3.next = ListNode(carry) 
        
#         return head.next