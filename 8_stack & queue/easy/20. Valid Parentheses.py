# use a dictionary for the relation between brackets
# use a stack to check if valid
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
#         if len(s) == 0:
#             return True
        
#         li = []
#         for i in s:
#             if i == '(':
#                 li.append(')')
#             elif i == '{':
#                 li.append('}')
#             elif i == '[':
#                 li.append(']')   
                
#             elif i == ')' or '}' or ']':
#                 if len(li) == 0:
#                     return False
#                 if li.pop() != i:
#                     return False
#             else:
#                 return False
#         if len(li) == 0:
#             return True
#         return False