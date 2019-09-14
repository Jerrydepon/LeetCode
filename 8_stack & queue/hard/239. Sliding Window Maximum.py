# as comments
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        result = []
        
        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if q and i - q[0] == k:
                q.popleft()
            
            while q:
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            
            q.append(i)
            
            if i >= k-1: # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])
            
        return result
        
#         if not nums:
#             return []

#         queue = collections.deque()
#         res = []
        
#         for i in range(k):
#             while len(queue) != 0:
#                 if nums[i] > nums[queue[-1]]:
#                     queue.pop()
#                 else:
#                     break
#             queue.append(i)
#         # print(queue)
        
#         for i in range(k, len(nums)):
#             res.append(nums[queue[0]])
            
#             if queue[0] < i - k + 1:
#                 queue.popleft()
                
#             while len(queue) != 0:
#                 if nums[i] > nums[queue[-1]]:
#                     queue.pop()
#                 else:
#                     break
#             queue.append(i)
            
#         res.append(nums[queue[0]])
#         return res