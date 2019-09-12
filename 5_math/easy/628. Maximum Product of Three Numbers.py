# sort array first
# only first 2 elements and last 3 elements can combine a maximum product
# itertools.combinations
import itertools
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) > 5:
            nums = nums[:3] + nums[-3:]
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])    
        # return max(a * b * c for a, b, c in itertools.combinations(nums, 3))