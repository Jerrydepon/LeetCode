class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        output, i = [], 0
        try:
            while intervals[i+1]:
                if intervals[i][1] >= intervals[i+1][0]:
                    intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                    del intervals[i+1]
                else:
                    i += 1
        except:
            return intervals