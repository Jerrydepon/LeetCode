# mind the use of key=lambda x: (-dic[x], x)
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.Counter()
        for word in words:
            dic[word] += 1
        
        return sorted(dic, key=lambda x: (-dic[x], x))[:k]
        