# recursive and remove one bit from each string for every step
# mind the 1+1 case
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0: 
            return b
        if len(b) == 0: 
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'        

#         a = a[::-1]
#         b = b[::-1]
        
#         if len(a) < len(b):
#             a += '0' * (len(b)-len(a))
#         else:
#             b += '0' * (len(a)-len(b))
        
#         s = ''
#         c = 0
#         for i in range(len(a)):
#             plus = int(a[i]) + int(b[i]) + c
#             if plus >= 2:
#                 word = str(plus % 2)
#                 c = 1
#             else:
#                 word = str(plus)
#                 c = 0
#             s += word
#         if c == 1:
#             s += '1'
            
#         return s[::-1]
                