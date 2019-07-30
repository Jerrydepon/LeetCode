class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        def frac(dx, dy):
            g = gcd(dx, dy)
            return (dx//g, dy//g)
        
        res = 0
        for i in range(len(points)):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                
                if dx == 0:
                    slope = 'i'
                else:
                    slope = frac(dx, dy)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            res = max(res, max(dic.values())+same)
            
        return res
          