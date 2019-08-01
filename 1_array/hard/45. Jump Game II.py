class Solution:
    def jump(self, nums: List[int]) -> int:
        res, start, end = 0, 0, 0
        while end < len(nums) - 1:
            res += 1
            reach = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return res
                reach = max(reach, i + nums[i])
            start, end = end + 1, reach
        return res
                   