class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        matrix_size = m * n

        left = 0
        right = matrix_size - 1

        while left <= right:
            mid = (right + left) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1

        return False 