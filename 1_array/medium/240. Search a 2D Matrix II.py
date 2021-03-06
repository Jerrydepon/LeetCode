# start searching for the bottom-left corner of the matrix
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: 
            return False

        row, col = len(matrix)-1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row-1
            else:
                col = col+1
        return False  