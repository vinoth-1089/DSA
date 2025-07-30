class solution:
    def set_zeros(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        first_row_zero = any(matrix[0][i] == 0 for i in range(m))
        first_col_zero = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0

        return matrix

# Test case
matrix = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1],
]

obj = solution()
result = obj.set_zeros(matrix)
for row in result:
    print(row)
