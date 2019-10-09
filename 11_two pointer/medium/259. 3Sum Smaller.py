# if (i,j,k) works, then (i,j,k), (i,j,k-1),...,(i,j,j+1) all work, totally (k-j) triplets
# similar to q.15, 16
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count        