class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        hash_set = set()

        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            right += 1
            max_len = max(max_len, len(hash_set))

        return max_len    