class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,2):
            for j in nums:
                ans.append(j)
        return ans        