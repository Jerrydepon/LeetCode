class Solution:
    def decodeString(self, s: str) -> str:
        num, stack = "", [["", 1]]
        for digit in s:
            if digit.isdigit():
                num += digit
            elif digit == "[":
                stack.append(["", int(num)])
                num = ""
            elif digit.isalpha():
                stack[-1][0] += digit
            elif digit == "]":
                char, times = stack.pop()
                stack[-1][0] += char*times  
            else:
                return False
        return stack[0][0]