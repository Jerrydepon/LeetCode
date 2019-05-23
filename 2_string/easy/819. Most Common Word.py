import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        paragraph = re.split(',|\.|!|,|\?|;|:|\'| ', paragraph)
        for word in paragraph:
            word = word.lower()
            if word == '':
                continue
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        for k in dic:
            if k in banned:
                dic[k] = 0
        return max(dic, key=dic.get)
                