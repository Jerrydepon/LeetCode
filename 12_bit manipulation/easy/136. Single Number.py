# import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = collections.Counter(nums)
        # return [i for i in count if count[i]==1][0]
        
        # without extra memory
        res = 0
        for num in nums:
            res ^= num # XOR 
        return res
    
    #       4   1   2   1   2
    #       100 001 010 001 010
    # res: 100 101 111 110 100