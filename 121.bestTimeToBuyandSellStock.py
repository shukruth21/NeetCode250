class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        curl= prices[0]
        for i in range(1,len(prices)):
            curr=prices[i]-curl
            profit = max(profit,curr)
            curl= min(curl,prices[i])
        return profit
