# initialize dictionary as {0:1}
# record the number of sum for each iteration
# check how many times of (total-target) exist to add to result
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, dic, total = 0, {0:1}, 0
        for num in nums:
            total += num
            res += dic.get(total-k, 0)
            dic[total] = dic.get(total, 0) + 1        
        return res