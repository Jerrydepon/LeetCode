# use heap to keep track of the highest building at certain position
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort()
        # print(events)
        
        res = [[0, 0]]
        hh = [(0, float('inf'))]
        for pos, negH, right in events:
            while hh[0][1] <= pos:
                heapq.heappop(hh)
            if negH:
                heapq.heappush(hh, (negH, right))
            if res[-1][1] != -hh[0][0]:
                res.append([pos, -hh[0][0]])
        return res[1:]

