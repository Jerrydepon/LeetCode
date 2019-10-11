# remainder: b << (x+1) --> b * (2,4,8...)
# number of count: 1 << x --> 2,4,8...
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0
            while a >= (b << (x + 1)): 
                x += 1
                print(x, b)
            res += (1 << x)
            a -= (b << x)
        return min(res if sig else -res, 2147483647) 
    