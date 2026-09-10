class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)

        for i in range(len(s2) - window_len + 1):
            sub_str = s2[i:i + window_len]
            if Counter(sub_str) == Counter(s1):
                return True

        return False