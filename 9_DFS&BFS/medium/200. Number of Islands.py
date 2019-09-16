# for each island count, make connected '1' into '#'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.setNeighbor(i, j, grid)
                    cnt += 1
        return cnt
                    
    def setNeighbor(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.setNeighbor(i+1, j, grid)
        self.setNeighbor(i-1, j, grid)
        self.setNeighbor(i, j+1, grid)
        self.setNeighbor(i, j-1, grid)