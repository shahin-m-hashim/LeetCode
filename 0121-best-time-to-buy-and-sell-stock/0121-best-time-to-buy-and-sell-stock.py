class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0  
        l, r = 0, 1  # Left (buy) and Right (sell) pointers

        while r < len(prices):  # Iterate while r is within bounds
            currentProfit = prices[r] - prices[l] #our current Profit
            if prices[l] < prices[r]:  # If buy price is less than sell price
                max_profit = max(max_profit, currentProfit)
            else:
                l = r  # Move buy pointer to r (new minimum price)
            r += 1  # Move sell pointer forward
        
        return max_profit
