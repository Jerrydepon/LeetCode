# if a whole number, push to the stack 
# do action depending on different signs
# (mind the division truncation)
class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
        for i, d in enumerate(s):
            if d.isdigit():
                num = 10 * num + int(d)
            if d in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num) 
                elif sign == '/':
                    stack.append(int(stack.pop() / num))   
                num = 0
                sign = d
                
        return sum(stack)