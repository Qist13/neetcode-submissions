class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                # Right sequence is strictly increasing
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # Right sequence is not strictly increasing
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1