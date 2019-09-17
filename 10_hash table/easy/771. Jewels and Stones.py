# make a dictionary containing jewels
# check how many jewels in the stone
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {}  # Map character to its frequency in S.
        res = 0  # Total number of jewels.
        
        for ch in J:
            if ch not in dic:
                dic[ch] = 1  
        for ch in S:
            if ch in dic:
                res += 1
                
        return res
        
#         output = 0
#         for stone in S:
#             if stone in J:
#                 output += 1
        
#         return output