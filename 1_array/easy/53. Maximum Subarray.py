# add upp each num step by step, 
# keep track of the largest sum, 
# set the sum to zero if its value is less than 0
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float('-inf')
        sum = 0
        for i, item in enumerate(nums):
            sum += item
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max