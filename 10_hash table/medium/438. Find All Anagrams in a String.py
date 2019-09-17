# use Counter to keep track of the counted elements in the scope
# add one, check equality, delete previous one (remember to delete if count==0)
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount = Counter(s[:len(p)-1])
        pCount = Counter(p)
        res = []
        for i in range(len(p)-1, len(s)):
            sCount[s[i]] += 1
            if sCount == pCount:
                res.append(i-len(p)+1)
            sCount[s[i-len(p)+1]] -= 1
            if sCount[s[i-len(p)+1]] == 0:
                del sCount[s[i-len(p)+1]]
        return res
        