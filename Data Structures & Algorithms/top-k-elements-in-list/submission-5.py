class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq_arr[c].append(num)
        
        most_freq = []

        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq
        
        return most_freq
