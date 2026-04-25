class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        
        return not any(arr)
        