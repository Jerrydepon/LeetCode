# convert time to minutes and sort the time
# append the smallest time plus 24 hours for difference between first and last
# use zip to create a list with diffence 
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minutes = list(map(convert, timePoints))
        minutes.sort()
        
        minutes.append(minutes[0] + 1440)
        return min(b - a for a, b in zip(minutes, minutes[1:]))     