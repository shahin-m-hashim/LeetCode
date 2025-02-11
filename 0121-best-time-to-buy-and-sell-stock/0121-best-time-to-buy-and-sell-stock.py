class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1  # Left (buy) and Right (sell) pointers
        max_profit = 0  

        while r < len(prices):  # Iterate while r is within bounds
            if prices[r] > prices[l]:  # If sell price is greater than buy price
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r  # Move buy pointer to r (new minimum price)
            r += 1  # Move sell pointer forward
        
        return max_profit
