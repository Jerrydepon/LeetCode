# similar to normal decimal calculation but use 26 as base
# ord()
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res*26 + ord(i)-ord('A')+1
        return res
        
        # s = s[::-1]
        # c = 1
        # out = 0
        # for dig in s:
        #     num = ord(dig) - 64
        #     out += num * c
        #     c *= 26
        # return out