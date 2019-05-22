class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li = [-1] * (len(nums)+1)
        for i in nums:
            li[i] = i
        for j, item in enumerate(li):
            if item == -1:
                return j