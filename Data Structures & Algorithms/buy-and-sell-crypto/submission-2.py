class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        buy = prices[0]
        profit, max_profit = 0,0

        for i in range(1,n):
            diff = prices[i] - buy
            if diff > profit:
                profit = diff
                max_profit = max(profit, max_profit)
            else:
                buy = min(buy, prices[i])

            

        return max_profit