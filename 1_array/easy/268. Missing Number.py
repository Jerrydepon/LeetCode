# make a list with (len(nums)+1) elements of -1
# iterate through numbers and set the index of number in the list euqal to number
# iterate through the list again and find the index with value equal to -1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li = [-1] * (len(nums)+1)
        for i in nums:
            li[i] = i
        for j, item in enumerate(li):
            if item == -1:
                return j