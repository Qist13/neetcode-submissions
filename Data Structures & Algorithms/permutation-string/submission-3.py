class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = Counter(s2[:len(s1)])

        if s1_map == s2_map:
            return True

        for i in range(len(s1), len(s2)):
            s2_map[s2[i]] += 1
            s2_map[s2[i - len(s1)]] -= 1

            if s1_map == s2_map:
                return True

        return False