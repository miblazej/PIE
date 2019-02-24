def sudoku_check(A):
    # check for duplicate in every row and in every column
    # column check
    for i in range(1, 10):
        for m in range(9):
            flag = 0
            for j in range(9):
                if i == A[m][j]:
                    flag += 1
        if flag > 1:
            return False
    # row check
    for i in range(1, 10):
        for m in range(9):
            flag = 0
            for j in range(9):
                if i == A[j][m]:
                    flag += 1
        if flag > 1:
            return False
    return True
