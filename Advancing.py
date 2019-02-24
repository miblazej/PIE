def adv(A):
    # Time:
    # Space:
    # Desc: Game simulator python book 5.4
    A_len = len(A)
    # start index
    i = 1
    best_choise, calc, position = 0, 0, 0
    step = 0
    while position + 1 < A_len:
        best_choise = 0
        calc = 0
        for i in range(position + 1, position + A[position] + 1):
            calc = i + A[i]
            if calc >= best_choise:
                best_choise = calc
                position = i
        if A[position] == 0:
            return False
        step += 1
    return step

A = [3, 1, 2, 3, 0, 0, 1]

C = (adv(A))
print(" " + str(C))
