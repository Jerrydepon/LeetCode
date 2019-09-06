# iterate through price and add profit to the sum profit if profit = (price[i]-price[-1]) > 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += (prices[i] - prices[i - 1])
        return res

