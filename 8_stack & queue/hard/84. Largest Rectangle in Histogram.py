class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        position, res = [-1], 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[position[-1]]:
                h = heights[position.pop()]
                w = i - position[-1] - 1
                res = max(res, h*w)
            position.append(i)
        return res
        