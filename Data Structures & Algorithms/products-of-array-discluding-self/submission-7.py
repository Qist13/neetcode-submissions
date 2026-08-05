class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prod = 1
        for i in range(len(prefix)):
            prefix[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(suffix) - 1, -1 ,-1):
            suffix[i] = prod
            prod *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
            
        return nums
    