class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            hash_map[diff] = i
        
        return []