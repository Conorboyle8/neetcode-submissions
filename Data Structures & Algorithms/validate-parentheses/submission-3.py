class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = { ")":"(", "}":"{", "]":"["}

        for i in s:
            if i in Map:
                if stack and stack[-1] == Map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False