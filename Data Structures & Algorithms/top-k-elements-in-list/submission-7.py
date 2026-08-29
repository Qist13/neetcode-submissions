class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        buckets = [[] for _ in range(len(nums))]

        for num, count in freq_map.items():
            buckets[count - 1].append(num)

        result = []

        for bucket in reversed(buckets):
            while bucket and k > 0:
                if bucket:
                    result.append(bucket.pop())
                    k -= 1

            if k == 0:
                break
                
        return result
