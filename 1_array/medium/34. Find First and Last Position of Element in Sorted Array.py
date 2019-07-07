class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        start = self.findStart(nums, target, l, r)
        end = self.findEnd(nums, target, l, r)
        
        return [start, end] if start <= end else [-1, -1]
        
    def findStart(self, nums, target, l, r):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
    def findEnd(self, nums, target, l, r):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r