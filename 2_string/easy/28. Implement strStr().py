# method 1: use haystack.find(needle)
# method 2: brutal force 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # # first method 
        # return haystack.find(needle)
        
        
        # second method
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1
        
        # # Or more concise way
        # for i in range(len(haystack) - len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
    
#         # third method
#         if len(needle) == 0:
#             return 0
#         if len(haystack) == 0:
#             return -1
        
#         hay_len = len(haystack)
#         nee_len = len(needle)
#         find = False
#         for i, a in enumerate(haystack):
#             if i+nee_len > hay_len:
#                 return -1
#             for j, b in enumerate(needle):
#                 if b == haystack[j+i]:
#                     find = True
#                 else:
#                     find = False
#                     break
#             if find == True:
#                 return i
#         return -1
                