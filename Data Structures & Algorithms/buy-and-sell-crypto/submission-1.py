class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        profit = 0

        for price in prices:
            if price > max_price:
                max_price = price
                profit = max(profit, max_price - min_price)
            elif price < min_price:
                min_price = price
                max_price = price

        return profit