class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = [0] * 26
        s2_chars = [0] * 26
        s1_len = len(s1)

        for ch in s1:
            s1_chars[ord(ch) - ord('a')] += 1
        
        left = 0
        right = len(s1)

        for ch in s2[:right]:
            s2_chars[ord(ch) - ord('a')] += 1

        if s1_chars == s2_chars:
            return True

        while right < len(s2):
            s2_chars[ord(s2[right]) - ord('a')] += 1
            s2_chars[ord(s2[left]) - ord('a')] -= 1

            if s1_chars == s2_chars:
                return True
                
            left += 1
            right += 1
        
        return False
