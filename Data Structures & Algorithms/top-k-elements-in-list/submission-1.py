class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        sorted_keys = [k for k, v in sorted(freq_map.items(),
                                    key=lambda x: x[1],
                                    reverse=True)]

        return sorted_keys[0:k]

        