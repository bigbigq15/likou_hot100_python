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