class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        for i in range(len(prices)):
            for y in range(i+1, len(prices)):
                if prices[y] - prices[i] > 0:
                    profit.append(prices[y] - prices[i])
        return max(profit)