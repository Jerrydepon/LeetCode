# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
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