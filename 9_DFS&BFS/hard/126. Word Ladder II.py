import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = w[:i] + c + w[i+1:]
                            if new_word in wordList:
                                newlayer[new_word] += [j+[new_word] for j in layer[w]]
                                
            wordList -= set(newlayer.keys())
            layer = newlayer
        
        return res
                                