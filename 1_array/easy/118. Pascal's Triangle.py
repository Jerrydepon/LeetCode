# assign 1's for peripheral and deal with add up later
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultset = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,  i):
                resultset[i][j] = resultset[i-1][j-1] + resultset[i-1][j]

        return resultset
        
        