# check possible way for each number of coins
# remember to check if valid solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-coin] if i-coin >= 0 else float('inf') for coin in coins]) + 1
        return -1 if dp[-1] == float('inf') else dp[-1]