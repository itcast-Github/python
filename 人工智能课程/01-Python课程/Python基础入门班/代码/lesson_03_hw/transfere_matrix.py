def transfer_matrix(matrix):
    if not matrix:
        return matrix
    rows = len(matrix)
    cols = len(matrix[0])
    ret = [[matrix[0][0]] * cols for i in range(rows)]
    for i in range(1, cols):
        ret[0][i] = ret[0][i - 1] + matrix[0][i]
    for i in range(1, rows):
        ret[i][0] = ret[i - 1][0] + matrix[i][0]
    for i in range(1, rows):
        for j in range(1, cols):
            ret[i][j] = ret[i - 1][j] + ret[i][j - 1] \
                        - ret[i - 1][j - 1] + matrix[i][j]
    return ret

print(transfer_matrix([[1, 2], [3, 4]]))
print(transfer_matrix([[1, 2, 3], [4, 5, 6]]))
print(transfer_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
