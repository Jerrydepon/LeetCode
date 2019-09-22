# sort first
# check if previous string was appeared in the set
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word        