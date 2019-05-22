class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        l = len(nums)
        tmp = None
        idx = 0
        i = 0
        while i < l:
            if nums[idx] == tmp:
                nums.remove(nums[idx])
            else:
                tmp = nums[idx]
                idx += 1 
            i += 1
        return idx