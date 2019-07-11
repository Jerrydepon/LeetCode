class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        output = 0
        for stone in S:
            if stone in J:
                output += 1
        
        return output