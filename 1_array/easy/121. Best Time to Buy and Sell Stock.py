# iterate through each price, and keep track of the minimum price as buy in value
# take each price as sell out value keep track of the maximum profit(sell-buy)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit