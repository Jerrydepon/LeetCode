from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # method 1: use combinations
        # output = [[]]
        # for i in range(1, len(nums)+1):
        #     output += combinations(nums, i)
        # return output
        
        # method 2
        self.output = [[]]
        for i, num in enumerate(nums):
            self.findSubset([num], nums[i+1:])
        return self.output
    
    def findSubset(self, subset, li):
        self.output.append(subset)
        if len(li) == 0:
            return
        for i, e in enumerate(li):
            self.findSubset(subset+[e], li[i+1:])
        