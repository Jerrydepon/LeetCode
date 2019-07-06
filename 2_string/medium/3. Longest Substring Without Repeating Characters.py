class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, start, dic = 0, 0, {}
        for i, d in enumerate(s):
            if d in dic and start <= dic[d]:
                start = dic[d] + 1
            else:
                max_length = max(max_length, i-start+1)
            dic[d] = i
        return max_length
        
                