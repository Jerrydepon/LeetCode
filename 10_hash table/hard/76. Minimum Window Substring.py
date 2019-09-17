# using missing to decide if containing all characters
# trick to find the real starting point
# change window if find smaller one
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        start, end, start_idx = 0, 0, 0
        for i, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                # find the real starting point if there are duplicated chars
                while need[s[start_idx]] < 0:
                    need[s[start_idx]] += 1
                    start_idx += 1
                    
                need[s[start_idx]] += 1
                missing += 1
                if end == 0 or i-start_idx < end-start:
                    start, end = start_idx, i
                start_idx += 1
                    
        return s[start:end]