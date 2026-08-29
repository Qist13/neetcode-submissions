class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_set = set(nums)
        max_len = 1

        for num in nums:
            if num + 1 not in hash_set:
                count = 1
                while num - 1 in hash_set:
                    num -= 1
                    count += 1
                max_len = max(max_len, count)   

        return max_len