class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()   # sort list
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                del stones[-1]
                del stones[-1]
            else:
                stones[-1] = stones[-1] - stones[-2]
                del stones[-2]
            stones.sort()
        return stones[0] if stones else 0




# find two heavest stones
# Take difference 
# if same both gone (make 0?)
# smaller dropped
# bigger gets difference
# return last stone