# insert interval if interval[1] < newInterval[0]
# insert newInterval if there is no overlap, and return result
# change newInterval if there is overlap, and keep looping through intervals
class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        res.append(newInterval)
        return res

