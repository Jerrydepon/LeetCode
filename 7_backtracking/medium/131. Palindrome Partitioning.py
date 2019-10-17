# classic DFS backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]])

    def isPal(self, s):
        return s == s[::-1]        