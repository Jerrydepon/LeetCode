class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            if matrix:
                res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res += [row.pop(-1)]
            if matrix:
                res += matrix.pop(-1)[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res += [row.pop(0)]
        return res
