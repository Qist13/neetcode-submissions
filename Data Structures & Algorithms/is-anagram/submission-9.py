class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in range(len(s)):
            dict1[s[i]] += 1
            dict2[t[i]] += 1
        
        return dict1 == dict2