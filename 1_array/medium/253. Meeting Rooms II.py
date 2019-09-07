# make two lists of sorted start time and sorted end time
# loop through start time (use two pointers to compare start and end time) 
# increase the number of rooms if there is no available rooms
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        
        available, rooms, s, e = 0, 0, 0, 0
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    rooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return rooms
        
        