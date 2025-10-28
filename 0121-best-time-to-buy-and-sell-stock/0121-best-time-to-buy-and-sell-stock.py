class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit= 0
        buy = prices[0]

        for price in prices:
            if price < buy: # if the current price is less than what we bought it on, we buy the current price 
                buy = price 
            else:
                max_profit=max(max_profit, price-buy)

        return max_profit