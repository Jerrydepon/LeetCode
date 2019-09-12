# trun [i**2:n:i] to False
# (mind the method of assigning False)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        numbers = [True] * n
        numbers[0] = numbers[1] = False
        for i in range(2, int(n**0.5+1)):
            if numbers[i]:
                numbers[i**2:n:i] = [False] * len(numbers[i**2:n:i])
        return sum(numbers)