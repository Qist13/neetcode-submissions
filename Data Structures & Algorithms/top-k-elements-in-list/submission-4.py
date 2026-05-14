class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        freq_arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hash_map[num] += 1
        
        for key, value in hash_map.items():
            freq_arr[value].append(key)

        result = []

        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return []
