def minesweeper(matrix):
    rn = len(matrix)
    cn = len(matrix[0])
    a = []
    for i in range(rn):
        b = []
        for j in range(cn):
            bombs = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if 0 <= k < rn:
                        if 0 <= l < cn:
                            bombs += matrix[k][l]
            b.append(bombs-matrix[i][j])
        a.append(b)
    return a


matrix = [[True, False, False], [False, True, False], [False, False, False]]

print(minesweeper(matrix))
