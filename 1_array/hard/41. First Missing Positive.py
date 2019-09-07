# nums.append(0) to avoid counting 0 as missing
# add len(nums) to numbers at the valid index (0 <= number < len(nums))
# check index till finding interger smaller than len(nums)
# if no missing, return len(nums)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(n):
            if nums[i] // n == 0:
                return i
        return n