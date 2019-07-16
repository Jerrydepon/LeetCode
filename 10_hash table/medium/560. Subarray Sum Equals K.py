class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output, dic, total = 0, {0:1}, 0
        for num in nums:
            total += num
            output += dic.get(total-k, 0)
            dic[total] = dic.get(total, 0) + 1        
        return output