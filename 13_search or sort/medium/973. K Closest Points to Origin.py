# use a dictionary to store key: index, value: distance
# sort the keys based on value and get the first K elements
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = {}
        for i, point in enumerate(points):
            dic[i] = point[0]**2 + point[1]**2
        index = sorted(dic.keys(), key=dic.get)[:K]
        return [points[j] for j in index]
        