class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        tmp = [""]
        for digit in digits:
            res = []
            for c in mapping[digit]:
                for i in tmp:
                    res.append(i+c)
            tmp = res
        return res
                    