# keep track of maximum destination for each element can reach, if at some position is not reachable, return False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i+num)
        return True
        