# too hard for now
import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        mapping = {}
        for i in range(len(words)):
            for j in range(len(words[i])):
                mapping[ord(words[i][j])-ord('a')] = set()
        
        letters = [0] * 26
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    key1 = ord(words[i][j]) - ord('a')
                    key2 = ord(words[i+1][j]) - ord('a')
                    if key2 not in mapping[key1]:
                        mapping[key1].add(key2)
                        letters[key2] += 1
                    break
        print(letters)
        print(mapping)

        res = ''
        queue = collections.deque()
        for i, letter in enumerate(letters):
            if letter == 0 and i in mapping:
                queue.append(i)
                
        while queue:
            word = queue.pop()
            res += chr(word + ord('a'))               
            next_set = mapping[word]
            for next_word in next_set:
                letters[next_word] -= 1
                if letters[next_word] == 0:
                    queue.append(next_word)
        
        if len(res) != len(mapping):
            return ''
        return res      