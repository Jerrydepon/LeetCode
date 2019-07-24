class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, res,  = 0, len(height)-1, 0
        tmp = min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] < tmp:
                    res += tmp - height[l]
                else:
                    tmp = min(height[l], height[r])
            else:
                r -= 1
                if height[r] < tmp:
                    res += tmp - height[r]
                else:
                    tmp = min(height[l], height[r])
        return res
                