class Solution(object):
    def coinChange(self, coins, amount):
        # Initialize dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Iterate through each coin
        for coin in coins:
            # Update dp for all amounts that can be made with the current coin
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        # If no solution, return -1
        return dp[amount] if dp[amount] != float('inf') else -1
