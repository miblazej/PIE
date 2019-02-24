def two_only(A, m):
    i = 0
    A_len = len(A)
    temp = min(2, m)
    count = 0
    while i < A_len:
        if A[i] == m and count < temp:
            i += 1
            count += 1
        elif A[i] == m and count >= temp:
            del A[i]
            A_len -= 1
        elif A[i] != m and count >= temp:
            break
        else:
            i += 1
    return A

A = [0, 1, 1, 2, 2, 2, 3, 3, 3]

B = two_only(A, 2)
print(B)
