# (res, sign)
# '(': append, ')': pop
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for word in s:
            if word.isdigit():
                num = 10*num + int(word)
            elif word == '+' or word == '-':
                res += sign*num
                num = 0
                sign = 1 if word=='+' else -1
            elif word == '(':
                stack.append((res, sign))
                res, sign = 0, 1
            elif word == ')':
                res += sign*num
                pre_res, pre_sign = stack.pop()
                res = res*pre_sign + pre_res
                num = 0
        res += num*sign
        return res
        
              