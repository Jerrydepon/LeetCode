# visit every connected node to it with a simple DFS. 
# seen will keep track of nodes that have been visited
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()
        def dfs(node):
            for i, friend in enumerate(M[node]):
                if friend and (i not in seen):
                    seen.add(i)
                    dfs(i)

        ans = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans          