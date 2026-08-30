class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            
            max_len = max(max_len, len(chars))
        
        return max_len