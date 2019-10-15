# put lower and upper into the nums first
# compare neighboring two numbers
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.insert(0, lower-1)
        nums.append(upper+1)
        res = []
        i = 0
        for i in range(len(nums)-1):
            left, right = nums[i], nums[i+1]
            if left != right-1:
                if right-left == 2:
                    res.append(str(right-1))
                elif right-left > 2:
                    res.append(str(left+1) + "->" + str(right-1))
        return res        
            