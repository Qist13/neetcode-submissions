class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest_price = prices[0]

        for price in prices:
            cheapest_price = min(cheapest_price, price)
            max_profit = max(max_profit, price - cheapest_price)
        
        return max_profit