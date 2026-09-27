class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0] #current lowest $ is 1st in list
        best = 0 #max profit so far
        for x in prices: # go thru each price in list
            if x < low: # is this price < lowest $
                low = x # if yes then its new lowest $
            best = max(best, x - low) #compare this profit against best so far
        return best