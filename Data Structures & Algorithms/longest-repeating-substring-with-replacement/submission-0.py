class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_arr = [0] * 26

        left = 0
        right = 0
        max_len = 0

        while right < len(s):
            freq_arr[ord(s[right]) - ord('A')] += 1

            most_freq = 0

            for i in range(len(freq_arr)):
                most_freq = max(most_freq, freq_arr[i])

            while (right - left + 1) - most_freq > k:
                freq_arr[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
        