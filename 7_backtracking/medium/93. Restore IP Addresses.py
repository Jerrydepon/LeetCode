# restriction on two and three digits
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.dfs(s, 0, "")
        return self.res

    def dfs(self, s, index, path):
        if index == 4:
            if not s:
                self.res.append(path[:-1])
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".")
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".")
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".")