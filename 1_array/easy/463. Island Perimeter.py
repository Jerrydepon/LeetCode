# if neighbor is water, peremeter plus 1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
#         self.peri, self.m, self.n = 0, len(grid), len(grid[0])
#         for i in range(self.m):
#             for j in range(self.n):
#                 if grid[i][j] == 1:
#                     self.searchNeighbor(i-1, j, grid)
#                     self.searchNeighbor(i+1, j, grid)
#                     self.searchNeighbor(i, j-1, grid)
#                     self.searchNeighbor(i, j+1, grid)
#         return self.peri
    
#     def searchNeighbor(self, i, j, grid):
#         if i<0 or j<0 or i==self.m or j==self.n or grid[i][j]==0:
#             self.peri += 1
        
    
        # faster method
        H, W = len(grid), len(grid[0])        
        area = 0
        connect = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    area += 1
                    # check up and left
                    if r > 0 and grid[r-1][c] == 1: connect += 1
                    if c > 0 and grid[r][c-1] == 1: connect += 1
        return area * 4 - 2 * connect
                  