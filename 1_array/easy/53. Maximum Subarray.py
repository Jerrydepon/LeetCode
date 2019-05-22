class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum = 0
        for _, item in enumerate(nums):
            sum += item
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi