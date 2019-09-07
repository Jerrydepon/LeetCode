# recode the product intergers before each element
# multpile by the product of integers after each element
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, product = [], 1
        for i in range(len(nums)):
            output.append(product)
            product *= nums[i]
        
        product = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= product
            product *= nums[j]
        
        return output