class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        arr = [0] * 26
        max_len = 1

        for right in range(len(s)):
            arr[ord(s[right]) - ord('A')] += 1

            while sum(arr) != max(arr) and sum(arr) - max(arr) > k:
                arr[ord(s[left]) - ord('A')] -= 1
                left += 1

            count = sum(arr)
            max_len = max(max_len, count)

        return max_len
