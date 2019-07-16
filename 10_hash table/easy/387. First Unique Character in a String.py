class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        
        dic = {}
        for i, item in enumerate(s):
            if item not in dic:
                dic[item] = i
            else:
                dic[item] = -1
                
        for _, v in dic.items():
            if v != -1:
                return v
        return -1