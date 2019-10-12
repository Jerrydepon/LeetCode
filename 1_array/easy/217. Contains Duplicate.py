import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count = collections.Counter(nums)
        # for k, v in count.items():
        #     if v >= 2:
        #         return True
        # return False
    
        # another method
        return len(nums) != len(set(nums))