class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for c in range(n):
                        if matrix[i][c] != 0:
                            matrix[i][c] = ''
                    for r in range(m):
                        if matrix[r][j] != 0:
                            matrix[r][j] = ''
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '':
                    matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any([0 == i[0] for i in matrix])
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i, x in enumerate(matrix[1:]):
            if x[0] == 0:
                for j in range(1, n):
                    x[j] = 0

        for i, x in enumerate(matrix[0][1:], start=1):
            if x == 0:
                for j in matrix[1:]:
                    j[i] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_zero:
            for x in matrix:
                x[0] = 0
