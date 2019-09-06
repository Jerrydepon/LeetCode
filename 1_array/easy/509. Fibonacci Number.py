# notice both recursive & iterative methods
class Solution:
    def fib(self, N: int) -> int:
        # # recursive
        # if N < 0:
        #     return False
        # if N == 0:
        #     return 0
        # if N == 1:
        #     return 1
        # return self.fib(N-1) + self.fib(N-2)
    
        # iterative
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        a, b = 0, 1
        for i in range(N):
            a, b = b, a+b
        return a