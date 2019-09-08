# pop last digit of two integers and sum up with carry
# add carry if carry remains in the end
# convert digit in the list to string by join and reverse
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = list(num1)
        nums2 = list(num2)
        res, carry = [], 0

        while nums1 or nums2:
            n1 = n2 = 0
            if nums1: n1 = ord(nums1.pop()) - ord('0')
            if nums2: n2 = ord(nums2.pop()) - ord('0')
            
            carry, remain = divmod(n1 + n2 + carry, 10)
            res.append(remain)
        
        if carry:
            res.append(carry)
        return ''.join(str(d) for d in res)[::-1]
        
#         num1 = num1[::-1]
#         num2 = num2[::-1]
#         if len(num1) < len(num2):
#             num1 += '0'*(len(num2)-len(num1))
#         else:
#             num2 += '0'*(len(num1)-len(num2))
        
#         s = ''
#         c = 0
#         for i in range(len(num1)):
#             add = ord(num1[i])-ord('0') + ord(num2[i])-ord('0') + c
#             c = add // 10
#             add = add % 10
#             s += str(add)
            
#         if c == 1:
#             s += '1'
#         s = s[::-1]
#         return s
        