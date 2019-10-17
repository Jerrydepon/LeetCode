# start with 1 -> second character
# check if index i reach the end
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits) - 1
        while i < n:
            if bits[i] == 1:
                i += 2
            else: 
                i += 1
        return i == n        