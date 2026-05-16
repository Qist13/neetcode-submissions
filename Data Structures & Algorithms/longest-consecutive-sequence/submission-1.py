class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()

        max_len = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
                
        return max(max_len, count)