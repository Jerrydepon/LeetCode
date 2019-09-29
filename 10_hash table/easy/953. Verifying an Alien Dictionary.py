# transfer the character to index order by hash table
# zip for comparison between adjacent words
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        words = [[dic[c] for c in word] for word in words]
        for w1, w2 in zip(words, words[1:]):
            if w1 > w2:
                return False
        return True       