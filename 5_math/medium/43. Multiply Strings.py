# multiply digit by digit
# pop out the preceding 0's in the number
# join back to string 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i, dig1 in enumerate(reversed(num1)):
            for j, dig2 in enumerate(reversed(num2)):
                res[i+j] += int(dig1) * int(dig2)
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10
    
        while len(res) > 1 and res[-1] == 0: 
            res.pop()
        return ''.join(map(str, res[::-1]))     