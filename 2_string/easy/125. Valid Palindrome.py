# use two pointers from start and end
# ignore digit if it's not number or alphabet
# check if two digits are the same
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True  
    
# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:        
#         if s == "":
#             return True
            
#         s = ''.join(re.split(', |: | |@|\.|#|-|\?|\'|\"|;|!|,|\(|\)|!|`|:', s))
#         s = s.lower()
#         if s == s[::-1]:
#             return True
#         return False