# sort the array first
# iterate from 0 to third to last number
# each number pairs with other two numbers from converging inward pointers
# mind how to deal with duplicated number
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        output = []
        nums = sorted(nums)
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                sum_ = num + nums[l] + nums[r]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    output.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return output