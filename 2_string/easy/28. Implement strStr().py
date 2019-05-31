class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
        hay_len = len(haystack)
        nee_len = len(needle)
        find = False
        for i, a in enumerate(haystack):
            if i+nee_len > hay_len:
                return -1
            for j, b in enumerate(needle):
                if b == haystack[j+i]:
                    find = True
                else:
                    find = False
                    break
            if find == True:
                return i
        return -1
                