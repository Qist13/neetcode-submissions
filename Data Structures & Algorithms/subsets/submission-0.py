class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets.extend(new_subsets)

        return subsets