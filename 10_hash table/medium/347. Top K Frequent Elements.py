# (defaultdict + Counter)
# key: cnt, value: integer
# extend result from the maximum possibility of frequency
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # method 1: defaultdict + Counter without sorting
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]
        
        # # method: sort
        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        # return sorted(dic.keys(), key=dic.get, reverse=True)[:k]