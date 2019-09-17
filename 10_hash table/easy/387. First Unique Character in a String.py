# count the occurrence of each character
# iterate through the string to find the character with only one occurrence
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    
#         if len(s) == 0:
#             return -1
        
#         dic = {}
#         for i, item in enumerate(s):
#             if item not in dic:
#                 dic[item] = i
#             else:
#                 dic[item] = -1
                
#         for _, v in dic.items():
#             if v != -1:
#                 return v
#         return -1