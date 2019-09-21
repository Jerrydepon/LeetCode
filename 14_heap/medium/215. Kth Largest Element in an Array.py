# mind the moethod between max heap and min heap
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # #  method 1: sorted -- O(nlogn)
        # if k > len(nums):
        #     return -1
        # nums = sorted(nums, reverse=True)
        # return nums[k-1]
        
        # # method 2: max heap -- O(n + klog(n))
        # nums = [-num for num in nums]
        # heapq.heapify(nums)
        # for _ in range(k):
        #     element = heapq.heappop(nums)
        # return -element
        
        # method 3: min heap -- O(k) + O((n-k) * logk)
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heapq.heapreplace(h, nums[i])
        return h[0]
        