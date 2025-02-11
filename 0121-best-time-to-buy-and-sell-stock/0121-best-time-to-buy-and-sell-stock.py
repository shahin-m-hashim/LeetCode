class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0  # Edge case: empty array
        
        max_profit = 0  # Track max profit
        min_price = float('inf')  # Track lowest price

        for price in prices:
            min_price = min(min_price, price)  # Update min_price if we find a lower price
            max_profit = max(max_profit, price - min_price)  # Update max_profit
            
        return max_profit