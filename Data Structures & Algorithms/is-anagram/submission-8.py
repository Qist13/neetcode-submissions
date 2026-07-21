class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for ch in s:
            dict1[ch] += 1
        
        for ch in t:
            dict2[ch] += 1
        
        return dict1 == dict2