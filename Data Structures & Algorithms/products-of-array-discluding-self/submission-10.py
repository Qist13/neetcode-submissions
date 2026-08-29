class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            results[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]
        
        return results
