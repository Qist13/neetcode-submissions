class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(clean_s) - 1

        while left < right:
            if clean_s[left] != clean_s[right]:
                return False

            left += 1
            right -= 1
        
        return True