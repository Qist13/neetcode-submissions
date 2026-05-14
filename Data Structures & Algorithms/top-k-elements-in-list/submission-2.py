class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        freq_arr = sorted(hash_map, key=lambda x: hash_map[x])

        result = []

        for i in range(k):
            result.append(freq_arr.pop())

        return result