class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.res = []
        self.findSum(candidates, target, [])
        
        return self.res
          
    def findSum(self, candidates, remain, tmp):      
        for i, digit in enumerate(candidates):
            if digit == remain:
                self.res.append(tmp+[digit])
            elif remain - digit > 0:
                self.findSum(candidates[i:], remain-digit, tmp+[digit])
            else:
                return