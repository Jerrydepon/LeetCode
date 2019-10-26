# BFS and check the reamining and the possible squares by layers
def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        li = []
        i = 1
        while i * i <= n:
            li.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in li:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt