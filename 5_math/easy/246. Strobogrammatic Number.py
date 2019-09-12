# use two pointers from two ends moving inward to check if in the specific set
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 0:
            return True
        l, r = 0, len(num)-1
        s = (('6', '9'), ('9', '6'), ('1', '1'), ('0', '0'), ('8', '8'))
        while l <= r:
            if (num[l], num[r]) not in s:
                return False
            l += 1
            r -= 1
        return True

