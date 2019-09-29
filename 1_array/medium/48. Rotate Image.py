# mind the range of i & j
# re-assign four positions for each rotation
# usage of '~' sign
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                        matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
                         