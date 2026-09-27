class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best = 0 
        for x in prices:
            if x < low:
                low = x
            best = max(best, x - low)
        return best