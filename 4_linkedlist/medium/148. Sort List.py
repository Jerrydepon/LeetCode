# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use pre, slow, fast pointers to divide linked list into two linked lists
# recursively merge thwo linked lists
class Solution:
    def sortList(self, head: ListNode) -> ListNode: 
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
    
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next

        tail.next = h1 or h2
        return dummy.next