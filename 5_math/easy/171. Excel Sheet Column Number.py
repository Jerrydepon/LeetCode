class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        c = 1
        out = 0
        for dig in s:
            num = ord(dig) - 64
            out += num * c
            c *= 26
        return out