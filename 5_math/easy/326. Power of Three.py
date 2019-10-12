# find the greatest power of 3 integer (in the range of 2**32 -> 32 bits)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        # 	return False
        # while n % 3 == 0:        	
        # 	n = n // 3
        # return True if n == 1 else False      
        
        # method without using loop / recursion
        # print(3**19, 2**32)
        return n > 0 and 3**19 % n == 0