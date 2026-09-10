class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        arr = [0] * 26
        max_len = 1
        max_freq = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            arr[idx] += 1
            max_freq = max(max_freq, arr[idx])

            while (right - left + 1) - max_freq > k:
                arr[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
