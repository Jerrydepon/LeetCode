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
        if ia + ib < k:
            if ma > mb:
                return self.searchMedian(a, b[ib+1:], i-ib-1)
            else:
                return self.searchMedian(a[ia+1:], b, i-ia-1)
        else:
            if ma > mb:
                return self.searchMedian(a[:ia], b, k)
            else:
                return self.searchMedian(a, b[:ib], k)