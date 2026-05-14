class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        freq_arr = [k for k in sorted(hash_map, key=lambda x: hash_map[x], reverse=True)]

        return freq_arr[:k]