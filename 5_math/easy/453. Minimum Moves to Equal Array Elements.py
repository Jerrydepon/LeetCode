# special math problem
# m: number of moves, n: size
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # sum + (n-1)*m = x*n
        # min + m = x
        return sum(nums) - min(nums)*len(nums)