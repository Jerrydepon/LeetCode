# use a heap for smaller numbers, and a heap for larger number
# mind the minus sign for smaller heap
# keep the difference of size of two heap no more than 1
# two cases for median
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
            return 
        if num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) - len(self.small) == 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        return -self.small[0] if len(self.small) > len(self.large) else self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()