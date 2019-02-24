def var1(A, key):
    A_len = len(A)
    i = 0
    elements = 0
    zeros = 0
    while elements + zeros < A_len:
        if A[i] != key and A[i] != 0:
            elements += 1
            i += 1
        elif A[i] == key:
            A[i] = 0
            zeros += 1
        elif A[i] == 0:
            A[i], A[i+zeros] = A[i+zeros], 0
    return elements

A = [1, 1, 2, 2, 3, 3]
print(var1(A, 1))
