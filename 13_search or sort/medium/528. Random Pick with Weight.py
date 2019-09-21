# build a cumulative weight array
# use binary search to find the index for random number
import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        for i in range(1, len(w)):
            w[i] += w[i-1]
        
    def pickIndex(self):     
        l, r = 0, len(self.w)-1
        rand_num = random.randint(1, self.total)
        while l < r:
            mid = (l+r) // 2
            if rand_num <= self.w[mid]:
                r = mid
            else:
                l = mid + 1 
        return l     
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()