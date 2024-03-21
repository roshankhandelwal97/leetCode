#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        profit = 0
        for i in prices: 
            if i < minP: 
                minP = i
            else: 
                profit = max(profit, i - minP)
        return profit
            
            

            
