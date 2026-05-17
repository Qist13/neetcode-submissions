class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        result = numbers[left] + numbers[right]

        while not result == target:
            if result > target:
                right -= 1
            elif result < target:
                left += 1
            result = numbers[left] + numbers[right]
        
        return [left + 1, right + 1]