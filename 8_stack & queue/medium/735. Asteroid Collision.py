# asteroids can be negative while they are in the beginning of array
# stack for right-most asteroid 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            elif asteroid < 0:
                while len(res) and res[-1] > 0:
                    if res[-1] == -asteroid: 
                        res.pop()
                        break
                    elif res[-1] < -asteroid:
                        res.pop()
                    elif res[-1] > -asteroid:
                        break
                else:
                    res.append(asteroid)
        return res        