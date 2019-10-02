# key: word, value: longest word chain
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # DP method
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i]+w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())  
    
    
#         # hash table method
#         words = sorted(words, key=lambda word:len(word))
#         word_dict = {}    
#         for word in words:
#             word_dict[word] = 1
        
#         longest = 1
#         for word in words:
#             for i in range(len(word)):
#                 if word[:i] + word[i + 1:] in word_dict:
#                     word_dict[word] = word_dict[word[:i] + word[i + 1:]] + 1
#                     longest = max(longest, word_dict[word])
        
#         return longest