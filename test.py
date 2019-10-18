# start searching for the bottom-left corner of the matrix
class Solution:
    def searchMatrix(self, row, col, matrix, targetRMP):
        if not matrix or not matrix[0]: 
            return False     

        r, c = row - 1, 0
        while r >= 0 and c < col:
            if matrix[r][c] == targetRMP:
                return (r, c)
            elif matrix[r][c] > targetRMP:
                r = r-1
            else:
                c = c+1
        return (-1, -1)
           