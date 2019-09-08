# replace "!?',;." with space
# loop through word in paragraph (split) and ignore the banned word
# count by dictionary, keep track of the largest count
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.": 
            paragraph = paragraph.replace(c, " ")
        dic, res, count = {}, "" , 0
        for word in paragraph.lower().split():
            if word in banned:
                continue;
            elif word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
            if dic[word] > count:
                count = dic[word]
                res = word
        return res     
    
# import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:        
        # dic = {}
        # paragraph = re.split(',|\.|!|,|\?|;|:|\'| ', paragraph)
        # for word in paragraph:
        #     word = word.lower()
        #     if word == '':
        #         continue
        #     if word in dic:
        #         dic[word] += 1
        #     else:
        #         dic[word] = 1
        # for k in dic:
        #     if k in banned:
        #         dic[k] = 0
        # return max(dic, key=dic.get)
                