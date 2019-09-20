# for each comparison, check if overlapping
# increase the index of list with lower right end each iteration
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res, a, b = [], 0, 0
        while a < len(A) and b < len(B):
            lower, upper = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            if lower <= upper:
                res.append([lower, upper])
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        
        return res