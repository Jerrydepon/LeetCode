class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        max_num = max(A)
#         for i, num in enumerate(A):
#             if num == max_num:
#                 return i
            
            
#         # use index
#         return A.index(max(A))
    
        
        # binary search
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m
        return l