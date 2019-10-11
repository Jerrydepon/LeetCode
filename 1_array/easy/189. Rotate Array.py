# cannot written as nums = nums[n-k:] + nums[:n-k]
# The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]   
        

#         # reverse in the place method
#         k, end = k % len(nums), len(nums) - 1
#         self.reverse(nums, 0, end - k)
#         self.reverse(nums, end - k + 1, end)
#         self.reverse(nums, 0, end)
        
#     def reverse(self, nums, start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1