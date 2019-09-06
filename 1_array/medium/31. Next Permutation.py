# find index i in the numbers where number at index i is smaller than the following number
# switch the number at index i with number larger than it (searching from the end)
# sort the numbers after index i
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or 0:
            return
        
        i, last_num, r = len(nums)-2, nums[-1], len(nums)-1
        while i >= 0 and nums[i] >= last_num:
            last_num = nums[i]
            i -= 1
        
        if i != -1:
            while i < r and nums[i] >= nums[r]:
                r -= 1
            nums[i], nums[r] = nums[r], nums[i]
            
        nums[i+1:] = sorted(nums[i+1:]) 
            