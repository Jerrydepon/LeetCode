class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         dic_s, dic_t = {}, {}
#         for i in range(len(s)):
#             dic_s[s[i]] = dic_s.get(s[i], []) + [i]
#             dic_t[t[i]] = dic_t.get(t[i], []) + [i]
        
#         return sorted(dic_s.values()) == sorted(dic_t.values())
    
        # faster method
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
        
        