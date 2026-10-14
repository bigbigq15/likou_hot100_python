class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0]) // 2
        left = 0
        right = len(matrix) - 1
        while n > 0:
            for i in range(left, right):
                x = matrix[left][i]
                matrix[left][i] = matrix[right - i + left][left]
                matrix[right - i + left][left] = matrix[right][right - i + left]
                matrix[right][right - i + left] = matrix[i][right]
                matrix[i][right] = x
            n -= 1
            left += 1
            right -= 1
