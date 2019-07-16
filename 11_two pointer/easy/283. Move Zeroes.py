class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for _, item in enumerate(nums):
            if item == 0:
                continue
            nums[idx] = item
            idx += 1
        
        for j in range(idx, len(nums)):
            nums[j] = 0