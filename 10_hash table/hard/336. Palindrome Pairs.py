# assign idx to word
# divide into prefix and suffix and check if palinfrome in two cases
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {word: i for i, word in enumerate(words)}
        res = []
        for word, i in dic.items():
            for j in range(len(word)+1):
                prev = word[:j]
                suf = word[j:]
                if prev == prev[::-1]: 
                    reverse = suf[::-1]
                    if reverse != word and reverse in dic:
                        res.append([dic[reverse], i])
                if j != len(word) and suf == suf[::-1]:
                    reverse = prev[::-1]
                    if reverse != word and reverse in dic:
                        res.append([i, dic[reverse]])    
        return res

