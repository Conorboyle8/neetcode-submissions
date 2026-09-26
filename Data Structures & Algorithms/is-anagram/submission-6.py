class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)
        if len(x) != len(y):
            return False
        for i in range(0, len(x or y)):
            if x[i] != y[i]:
                return False
        return True