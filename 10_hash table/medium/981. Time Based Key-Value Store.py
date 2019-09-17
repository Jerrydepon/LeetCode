# bisect: https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# use two defaultdict(list) to keep track of values and timestamp
# index of timestamp relates to element in value
import collections, bisect

class TimeMap:
    def __init__(self):
        self.values = collections.defaultdict(list)
        self.times = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i-1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)