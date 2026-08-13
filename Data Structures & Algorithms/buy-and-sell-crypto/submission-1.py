class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        curProfit = 0

        for i in range(1, len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
            else:
                curProfit = prices[i] - minPrice
                maxProfit = max(curProfit, maxProfit)
        return maxProfit
        