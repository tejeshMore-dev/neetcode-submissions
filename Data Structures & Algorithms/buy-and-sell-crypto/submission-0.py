class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        min_p = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            cur_profit = price - min_p
            profit = max(cur_profit, profit)
            min_p = min(min_p, price)
        
        return profit