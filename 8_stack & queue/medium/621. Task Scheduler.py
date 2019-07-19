from heapq import heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res, heap = 0, []
        for k, v in collections.Counter(tasks).items():
            heappush(heap, (-v, k))
        
        while heap:
            interval, tmp = 0, []
            while interval <= n:
                res += 1
                if heap:
                    v, k = heappop(heap)
                    if v != -1:
                        tmp.append((v+1, k))
                if not heap and not tmp:
                    break
                interval += 1
            for s in tmp:
                heappush(heap, s)      
        return res