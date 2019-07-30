import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        queue = collections.deque()
        res = []
        
        for i in range(k):
            while len(queue) != 0:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
        
        for i in range(k, len(nums)):
            res.append(nums[queue[0]])
            
            if queue[0] < i - k + 1:
                queue.popleft()
                
            while len(queue) != 0:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
            
        res.append(nums[queue[0]])
        return res