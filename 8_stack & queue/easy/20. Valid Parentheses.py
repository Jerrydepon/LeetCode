class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        li = []
        for i in s:
            if i == '(':
                li.append(')')
            elif i == '{':
                li.append('}')
            elif i == '[':
                li.append(']')   
                
            elif i == ')' or '}' or ']':
                if len(li) == 0:
                    return False
                if li.pop() != i:
                    return False
            else:
                return False
        if len(li) == 0:
            return True
        return False