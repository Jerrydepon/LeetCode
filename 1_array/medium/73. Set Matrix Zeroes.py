# try to use constant space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # zeros = []
        # row, col = len(matrix), len(matrix[0])
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             zeros.append((i, j))
        # for i, j in zeros:
        #     for c in range(col):
        #         matrix[i][c] = 0
        #     for r in range(row):
        #         matrix[r][j] = 0
        
        # use less space
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for tmp in range(row):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(col):
                        if matrix[i][tmp] != 0: 
                            matrix[i][tmp] = 'a'
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0