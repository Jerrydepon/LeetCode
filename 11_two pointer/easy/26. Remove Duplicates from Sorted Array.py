# iterate through the nums and use a tail pointer for the index of new array
# if num is different from the tail pointer, modify nums[newTail+1] inplace
# move tail pointer to the next index
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1        
        
#         if len(nums) == 0:
#             return 0
        
#         l = len(nums)
#         tmp = None
#         idx = 0
#         i = 0
#         while i < l:
#             if nums[idx] == tmp:
#                 nums.remove(nums[idx])
#             else:
#                 tmp = nums[idx]
#                 idx += 1 
#             i += 1
#         return idx