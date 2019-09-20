# use a pointer for putting number, which move to next if number is not zero
# use another pointer to iterate through nums
# after iteration, put zeros from index to the end
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