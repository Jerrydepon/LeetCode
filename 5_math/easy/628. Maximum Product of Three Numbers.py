import itertools
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) > 5:
            nums = nums[:3] + nums[-3:]
        return max(a * b * c for a, b, c in itertools.combinations(nums, 3))