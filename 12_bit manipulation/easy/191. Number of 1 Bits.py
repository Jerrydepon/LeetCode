# n &= n - 1 to eleminate 1 bit at the end
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(n)
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c   
    
    
        # return bin(n).count('1')