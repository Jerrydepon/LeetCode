# convert to string and check if palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # method1: Convert to string
        s = str(x)       
        return s == s[::-1]
    
        # # method2: Without converting to string
        # li = []
        # if x < 0:
        #     return False
        # while x > 0:
        #     digit = x % 10
        #     li.append(digit)
        #     x = x // 10
        # return li == li[::-1]