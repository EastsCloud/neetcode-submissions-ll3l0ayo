class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ''.join(c for c in s if c.isalnum()).lower()
        if cs == ''.join(reversed(cs)):
            return True
        return False