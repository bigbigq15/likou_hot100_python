from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        row = 0
        while True:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target and col != len(matrix[0]) - 1:
                col += 1
            elif matrix[row][col] > target or col == len(matrix[0]) - 1:
                row += 1
                if row == len(matrix):
                    break
                while True:
                    if matrix[row][col] > target and col > 0:
                        col -= 1
                        continue
                    elif matrix[row][col] == target:
                        return True
                    else:
                        break
        return False
