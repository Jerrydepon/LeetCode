# one line solution
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
#         res = [""] * n
#         for i in range(1, len(res)+1):
#             if i % 3 == 0 and i % 5 == 0:
#                 res[i-1] = "FizzBuzz"
#             elif i % 3 == 0:
#                 res[i-1] = "Fizz"
#             elif i % 5 == 0:
#                 res[i-1] = "Buzz"
#             else:
#                 res[i-1] = str(i)
#         return res
    
        # better method
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]