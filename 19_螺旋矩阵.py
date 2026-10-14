class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_left = 0
        row_right = len(matrix)
        col_left = 0
        col_right = len(matrix[0])
        res = []
        while col_left < col_right - 1 and row_left < row_right - 1:
            for i in range(col_left, col_right - 1):
                res.append(matrix[row_left][i])
            for i in range(row_left, row_right - 1):
                res.append(matrix[i][col_right - 1])
            for i in range(col_right - 1, col_left, -1):
                res.append(matrix[row_right - 1][i])
            for i in range(row_right - 1, row_left, -1):
                res.append(matrix[i][col_left])
            row_right -= 1
            row_left += 1
            col_right -= 1
            col_left += 1
        if col_right - 1 == col_left and row_left != row_right - 1:
            for i in range(row_left, row_right):
                res.append(matrix[i][col_right - 1])
        elif col_right - 1 != col_left and row_left == row_right - 1:
            for i in range(col_left, col_right):
                res.append(matrix[row_left][i])
        elif col_right - 1 == col_left and row_left == row_right - 1:
            res.append(matrix[row_right - 1][col_right - 1])
        return res
