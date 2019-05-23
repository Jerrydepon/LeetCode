class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        if len(a) < len(b):
            a += '0' * (len(b)-len(a))
        else:
            b += '0' * (len(a)-len(b))
        
        s = ''
        c = 0
        for i in range(len(a)):
            plus = int(a[i]) + int(b[i]) + c
            if plus >= 2:
                word = str(plus % 2)
                c = 1
            else:
                word = str(plus)
                c = 0
            s += word
        if c == 1:
            s += '1'
            
        return s[::-1]
                