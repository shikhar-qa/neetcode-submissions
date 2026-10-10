class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(0,len(prices)):
            max_remain = max(prices[i:len(prices)])
            if (max_remain - prices[i]) > max_profit:
                max_profit = max_remain - prices[i]
        return (max_profit)    

        