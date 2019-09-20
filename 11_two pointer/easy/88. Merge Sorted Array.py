# compare from last number of both arrays and put larger number into the tail of nums1
# remember to merge the remaining numbers from nums2 if nums1 is consumed up first
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # method 1 -- too slow
        # idx = 0
        # i = 0
        # j = 0
        # tmp_list = nums1[:m]
        # while m > 0 and n > 0:
        #     if tmp_list[i] <= nums2[j]:
        #         nums1[idx] = tmp_list[i]
        #         i += 1
        #         m -= 1
        #     else:
        #         nums1[idx] = nums2[j]
        #         j += 1
        #         n -= 1
        #     idx += 1
        # while m > 0:
        #     nums1[-m] = tmp_list[i]
        #     i += 1
        #     m -= 1
        # while n > 0:
        #     nums1[-n] = nums2[j]
        #     j += 1
        #     n -= 1
        
        # method 2 -- not formal
        # while n > 0:
        #     nums1[-n] = nums2[n-1]
        #     n -= 1
        # nums1.sort()

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1