class Solution:
    def calculate(self, s: str) -> int:
        def operation(op, second, first):
            if op == '+':
                return first + second
            elif op == '-':
                return first - second
            elif op == '*':
                return first * second
            elif op == '/':
                return first // second
            
        def precedence(current_op, prev_op):
            if prev_op == '(' or prev_op == ')':
                return False
            if (current_op == '*' or current_op == '/') and (prev_op == '+' or prev_op == '-'):
                return False
            return True
        
        if not s:
            return 0
        nums, ops, i = [], [], 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            elif c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                    i += 1
                nums.append(num)
            elif c == "(":
                ops.append(c)
                if s[i+1] == '-':
                    nums.append(0)
            elif c == ")":
                while ops[-1] != '(':
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in ['+', '-', '*', '/']:
                while len(ops) != 0 and precedence(c, ops[-1]):
                    if len(nums) > 1:
                        nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                    else:
                        nums.append(operation(ops.pop(), nums.pop(), 0))
                ops.append(c)
            i += 1
            
        while len(ops) > 0:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            
        return nums[0]