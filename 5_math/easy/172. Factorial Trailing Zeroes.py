# find number of 5 in the factorial
# 25 has two 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCnt = 0
        while n > 0:
            n = n//5 
            zeroCnt += n
        
        return zeroCnt        