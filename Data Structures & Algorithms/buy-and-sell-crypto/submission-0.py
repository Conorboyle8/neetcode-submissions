class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        x = 0
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > 0 and prices[j]-prices[i] > x:
                    x = prices[j]-prices[i]
                    print(j,i)
        return x