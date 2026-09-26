class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = s[::-1]
        cleaned = re.sub(r'[^A-Za-z0-9]', '', b)
        s2 = re.sub(r'[^A-Za-z0-9]', '', s)
        b2 = cleaned.lower()
        s3 = s2.lower()
        print(b2)
        print(s3)
        if b2 == s3:
            return True
        else:
            return False