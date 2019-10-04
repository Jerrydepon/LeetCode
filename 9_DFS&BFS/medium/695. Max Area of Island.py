# search neighbor lands when find an island
# mark the searched land out
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n, self.area, self.max_area = len(grid), len(grid[0]), 0, 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.area = 0
                    self.findIsland(i, j, grid)
        return self.max_area
                    
    def findIsland(self, i, j, grid):
        if i<0 or j<0 or i==self.m or j==self.n or grid[i][j]!=1:
            return
        self.area += 1
        grid[i][j] = -1
        self.max_area = max(self.area, self.max_area)
        self.findIsland(i-1, j, grid)
        self.findIsland(i+1, j, grid)
        self.findIsland(i, j-1, grid)
        self.findIsland(i, j+1, grid)
            