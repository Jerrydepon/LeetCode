# odd and even cases
# check if median index exist in the larger or smaller part of the array
# trim the array
# (mind the tricks) 
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        length = len(A) + len(B)
        if length % 2 == 1:
            return self.searchMedian(A, B, length//2)
        else:
            return (self.searchMedian(A, B, length//2-1) + self.searchMedian(A, B, length//2)) / 2
            
    def searchMedian(self, a, b, i):
        if not b:
            return a[i]
        if not a:
            return b[i]
        
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        # i-th element still exist in some larger part of the array
        if ia + ib < i:
            if ma > mb:
                # if a's median is bigger than b's, b's first half doesn't include i
                return self.searchMedian(a, b[ib+1:], i-ib-1)
            else:
                return self.searchMedian(a[ia+1:], b, i-ia-1)
        # i-th element still exist in some smaller part of the array
        else:
            if ma > mb:
                # if a's median is bigger than b's, a's second half doesn't include i
                return self.searchMedian(a[:ia], b, i)
            else:
                return self.searchMedian(a, b[:ib], i)