class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.longPath = 0
        self.dic = {}
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path = self.dfsSearch(i, j, -1)
        
        return self.longPath
    
    def dfsSearch(self, i, j, prev):
        if i<0 or i==len(self.matrix) or j<0 or j==len(self.matrix[0]) or self.matrix[i][j]<=prev:
            return 0
        
        if (i, j) in self.dic:
            return self.dic[(i, j)]
        
        cur = self.matrix[i][j]
        path = 1 + max(self.dfsSearch(i-1, j, cur),
                       self.dfsSearch(i, j-1, cur),
                       self.dfsSearch(i+1, j, cur),
                       self.dfsSearch(i, j+1, cur))
        
        self.longPath = max(self.longPath, path)
        self.dic[(i, j)] = path
        return path
        