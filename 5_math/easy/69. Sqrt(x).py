# use binary search to find the number in the range of mid**2 <= x < (mid+1)**2
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l, r = 0, x
        while True:
            mid = (l+r) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                r = mid-1
            elif mid**2 < x:
                l = mid+1
                