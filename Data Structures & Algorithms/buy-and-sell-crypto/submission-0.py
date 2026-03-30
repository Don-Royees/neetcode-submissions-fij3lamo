class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)):
            for x in range(i,len(prices)):
                if prices[x]-prices[i] > maxP:
                    maxP= prices[x]-prices[i]
        return maxP            
        