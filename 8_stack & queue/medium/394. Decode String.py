# [tmp_string, times]
# isdigit() : deal with times
# "[" : append
# "]" : pop
# isalpha : add character
class Solution:
    def decodeString(self, s: str) -> str:
        num, stack = "", [["", 1]]
        for d in s:
            if d.isdigit():
                num += d
            elif d == "[":
                stack.append(["", int(num)])
                num = ""
            elif d.isalpha():
                stack[-1][0] += d
            elif d == "]":
                char, times = stack.pop()
                stack[-1][0] += char*times  
            else:
                return False
        return stack[0][0]