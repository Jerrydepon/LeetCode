# find out the shortest string
# iterate through each word and check if the prefix equal to other strings
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
        
#         if len(strs) == 0:
#             return ""
        
#         num_words = len(strs)
#         sm_word_len = len(min(strs, key=lambda x: len(x)))
#         first = strs[0]
#         out = ""
#         for i in range(sm_word_len):
#             for j in range(1, num_words):
#                 if strs[j][i] != first[i]:
#                     return out
#             out += first[i]        
#         return out
                