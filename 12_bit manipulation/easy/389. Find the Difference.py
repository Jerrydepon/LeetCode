#  mind the XOR method to exclude duplicate characters (with aid of ord)
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # count = collections.Counter(s)
        # for cha in t:
        #     count[cha] -= 1
        # return [i for i in count if count[i]==-1][0]
    
        # XOR method
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)