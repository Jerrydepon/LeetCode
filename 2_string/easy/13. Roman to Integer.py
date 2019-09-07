# minus the sum with the number if it is smaller than its following number
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]
    
#         if len(s) == 0:
#             return 0
        
#         s = s.replace('IV', 'a')
#         s = s.replace('IX', 'b')
#         s = s.replace('XL', 'c')
#         s = s.replace('XC', 'd')
#         s = s.replace('CD', 'e')
#         s = s.replace('CM', 'f')
        
#         sum = 0
#         for word in s:
#             if word == 'I':
#                 sum += 1
#             elif word == 'V':
#                 sum += 5
#             elif word == 'X':
#                 sum += 10
#             elif word == 'L':
#                 sum += 50
#             elif word == 'C':
#                 sum += 100
#             elif word == 'D':
#                 sum += 500
#             elif word == 'M':
#                 sum += 1000
#             elif word == 'a':
#                 sum += 4
#             elif word == 'b':
#                 sum += 9
#             elif word == 'c':
#                 sum += 40
#             elif word == 'd':
#                 sum += 90
#             elif word == 'e':
#                 sum += 400
#             elif word == 'f':
#                 sum += 900
#             else:
#                 return False
#         return sum