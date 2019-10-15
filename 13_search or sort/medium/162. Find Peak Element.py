# find mid, compare it with its left and right neighbors  
# return mid if nums[mid] greater than both neighbors
# take the right half array if nums[mid] smaller than right neighbor
# otherwise, take the left half
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left