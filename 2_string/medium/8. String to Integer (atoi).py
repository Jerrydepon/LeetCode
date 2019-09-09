# based on RegEx -- re.findall (https://en.wikipedia.org/wiki/Regular_expression)
# deal with integer range
# use try-except to catch invalid number
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        s = re.findall('(^[\+\-]*\d+)', s)
        print(s)
        try:
            res = int(''.join(s))
            max_, min_ = 2**31 - 1, -2 ** 31
            if res > max_:
                return max_
            elif res < min_:
                return min_
            return res
            
        except:
            return 0