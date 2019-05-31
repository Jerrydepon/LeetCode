class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            num1 += '0'*(len(num2)-len(num1))
        else:
            num2 += '0'*(len(num1)-len(num2))
        
        s = ''
        c = 0
        for i in range(len(num1)):
            add = ord(num1[i])-ord('0') + ord(num2[i])-ord('0') + c
            c = add // 10
            add = add % 10
            s += str(add)
            
        if c == 1:
            s += '1'
        s = s[::-1]
        return s
        