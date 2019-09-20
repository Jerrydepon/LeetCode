# from two ends, calculate the maximum containing water by two walls
# keep track of the maximum result
# converge inward and keep the higher wall
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, res = 0, len(height)-1, 0
        while l < r:
            res = max(res, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res