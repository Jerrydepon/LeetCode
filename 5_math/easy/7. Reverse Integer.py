class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        neg = False
        if s[0] == '-':
            neg = True
            s = s.replace('-', '')
        
        s = int(s[::-1])
        if neg:
            s *= -1     
        if s < -(2**31) or s > 2**31-1:
            return 0
        return s