import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
            
        s = ''.join(re.split(', |: | |@|\.|#|-|\?|\'|\"|;|!|,|\(|\)|!|`|:', s))
        s = s.lower()
        if s == s[::-1]:
            return True
        return False