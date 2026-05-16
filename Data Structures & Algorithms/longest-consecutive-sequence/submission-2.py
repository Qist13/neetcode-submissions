class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        hash_set = set(nums)

        max_len = 1
        
        for num in hash_set:
            seq_start = num
            count = 0
            if not seq_start - 1 in hash_set:
                while seq_start in hash_set:
                    count += 1
                    seq_start += 1
            if count > max_len:
                max_len = count

        return max_len