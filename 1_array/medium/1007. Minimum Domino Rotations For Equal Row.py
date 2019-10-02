# iterate through number 1~6, if total number of i-th dominos minus repetition equals to the length of row, 
# there is a possible solution. Find the minimum rotation bewteen A and B.
from collections import Counter

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) != len(B): 
            return -1
        same, countA, countB = Counter(), Counter(A), Counter(B)
        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]        
        return -1