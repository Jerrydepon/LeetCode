# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# find the difference in length of two lists
# move (difference) steps from head of longer list
# move one step for each list to find the match
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        cnt_a = 0
        cnt_b = 0
        hA, hB = headA, headB
        while headA:
            cnt_a += 1
            headA = headA.next
        while headB:
            cnt_b += 1
            headB = headB.next
            
        if cnt_a > cnt_b:
            hA, hB = hB, hA    
        diff = abs(cnt_a - cnt_b)
        
        for _ in range(diff):
            hB = hB.next
            
        while hA:
            if hA == hB:
                return hA
            hA = hA.next
            hB = hB.next
        return None
        