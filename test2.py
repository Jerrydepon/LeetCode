import sys
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: 
            return 0
        
        longPath = 0
        self.matrix = matrix
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                path = self.dfs(r, c)
                longPath = max(longPath, path)
        return longPath


    def dfs(self, i, j):
        path = 0
        cur = self.matrix[i][j]
        self.matrix[i][j] = '#'
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                next_i = i + dx
                next_j = j + dy
                if (    0 <= next_i < len(self.matrix)
                        and 0 <= next_j < len(self.matrix)
                        and self.matrix[next_i][next_j] != '#'
                        and abs(cur - self.matrix[next_i][next_j]) > 3):
                    path = max(path, self.dfs(next_i, next_j))
        self.matrix[i][j] = cur
        return path + 1

    #     longPath = 0
    #     self.matrix = matrix
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             path = self.dfsSearch(r, c, sys.maxsize)
    #             longPath = max(longPath, path)
    #     return longPath
    
    # def dfsSearch(self, i, j, prev):
    #     if i<0 or i==len(self.matrix) or j<0 or j==len(self.matrix[0]) or self.matrix[i][j]=='#' or abs(self.matrix[i][j]-prev)<=3:
    #         return 0
    #     cur = self.matrix[i][j]
    #     self.matrix[i][j] = '#'
    #     path = 1 + max(self.dfsSearch(i-1, j, cur),
    #                    self.dfsSearch(i, j-1, cur),
    #                    self.dfsSearch(i+1, j, cur),
    #                    self.dfsSearch(i, j+1, cur),
    #                    self.dfsSearch(i-1, j-1, cur),
    #                    self.dfsSearch(i-1, j+1, cur),
    #                    self.dfsSearch(i+1, j-1, cur),
    #                    self.dfsSearch(i+1, j+1, cur))
    #     self.matrix[i][j] = cur
    #     return path

a = [[8,2,4],[0,6,1],[3,7,9]]
# a = [[7,1,5,7],[2,8,3,9],[3,6,1,4],[5,1,7,3]]
print(Solution().longestIncreasingPath(a))