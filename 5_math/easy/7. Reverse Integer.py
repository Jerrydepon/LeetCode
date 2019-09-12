# get absolute value of input
# reverse number
# check range (0x7FFFFFFF)
# return number with sign
class Solution:
    def reverse(self, x: int) -> int:
        m = -1 if x < 0 else 1
        x = x * m
        
        n = 0
        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10
        
        if n > 0x7FFFFFFF:
            return 0

        return n * m
    
#         s = str(x)
#         neg = False
#         if s[0] == '-':
#             neg = True
#             s = s.replace('-', '')
        
#         s = int(s[::-1])
#         if neg:
#             s *= -1     
#         if s < -(2**31) or s > 2**31-1:
#             return 0
#         return s