# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            value, idx, node = heap[0]
            if not node.next:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (node.next.val, idx, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next
                