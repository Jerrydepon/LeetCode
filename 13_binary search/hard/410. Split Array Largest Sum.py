class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l+h) // 2
            if self.valid(mid, nums, m):
                h = mid
            else:
                l = mid + 1
        return l
    
    def valid(self, mid, nums, m):
        num_array, sum_sub = 0, 0        
        for num in nums:
            sum_sub += num
            if sum_sub > mid:
                num_array += 1
                sum_sub = num
            if num_array == m:
                return False
        return True        
    