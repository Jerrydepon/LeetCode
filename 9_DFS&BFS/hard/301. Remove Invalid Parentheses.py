# count l and r (if l != 0, minus first if meets r)
# number of l and r + remaining excess l and r
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                if l != 0:
                    l -= 1
                else: 
                    r += 1
                    
        self.res = []
        self.findValidParentheses(0, 0, 0, l, r, s, '')
        return set(self.res)
    
    def findValidParentheses(self, idx, l, r, l_rem, r_rem, s, out):
        if idx == len(s):
            if l == r and l_rem == r_rem == 0:
                self.res.append(out)
            return
        else:
            if s[idx] == '(':
                if l_rem > 0:
                    self.findValidParentheses(idx+1, l, r, l_rem-1, r_rem, s, out)
                self.findValidParentheses(idx+1, l+1, r, l_rem, r_rem, s, out+s[idx])
            elif s[idx] == ')':
                if l > r:
                    self.findValidParentheses(idx+1, l, r+1, l_rem, r_rem, s, out+s[idx])
                if r_rem > 0:
                    self.findValidParentheses(idx+1, l, r, l_rem, r_rem-1, s, out)
            else:
                self.findValidParentheses(idx+1, l, r, l_rem, r_rem, s, out+s[idx])

