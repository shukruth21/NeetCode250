class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        curl=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<curl):
                curl=prices[i]
            elif(i==len(prices)-1 or  prices[i]>prices[i+1]):
                profit+=prices[i]-curl
                curl=prices[i]
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit

