class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = r = n
        tmp = ""
        self.res = []
        self.appendParenthesis(l, r, tmp)
        return self.res
    
    def appendParenthesis(self, l, r, tmp):
        if l == 0 and r == 0:
            self.res.append(tmp)
        if l > 0:
            self.appendParenthesis(l-1, r, tmp+"(")
        if r > 0 and r > l:
            self.appendParenthesis(l, r-1, tmp+")")