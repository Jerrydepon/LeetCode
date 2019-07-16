class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # brute force
#         if len(nums) < 2:
#             return 0
        
#         for i, item_i in enumerate(nums):
#             rem = target - item_i
#             for j, item_j in enumerate(nums[i+1:]):
#                 if item_j == rem:
#                     return [i, i+j+1]
#         return 0
    
        # hash table
        dict = {}
        for i, item in enumerate(nums):
            if item in dict:
                return [dict[item], i]
            else:
                dict[target-item] = i