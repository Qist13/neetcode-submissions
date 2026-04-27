class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagrams_map[key].append(s)
        
        return list(anagrams_map.values())