# if find a word in the dictionary, mark the position of new starting point as 1
# check if reaching the end of input
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [0] * (len(s)+1)
        self.findWord(s, wordDict, res, 0)
        
        return res[-1] == 1
    
    def findWord(self, s, wordDict, res, start):
        if start >= len(s):
            return
        for word in wordDict:
            end = start+len(word)
            if s[start:end] == word and res[end] == 0:
                res[end] = 1
                self.findWord(s, wordDict, res, end)