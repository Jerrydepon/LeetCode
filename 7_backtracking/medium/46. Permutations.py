class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.addPermute(nums, [])  
        return self.output
    
    def addPermute(self, nums, tmp):
        if nums == []:
            self.output.append(tmp)
        for i, num in enumerate(nums):
            self.addPermute(nums[:i]+nums[i+1:], tmp+[num])
            