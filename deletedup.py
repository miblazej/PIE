def delete_dup_and_shift(A):
    # T = O(n)
    # S = O(n)
    # Desc. Function that deletes duplicates and shifts
    A_len = len(A) - 1
    i = 0
    zeros = 0
    while i + zeros < A_len:
        if A[i] == A[i+1]:
            A[i+1] = 0
            zeros += 1
        elif A[i] != A[i+1] and A[i+1] != 0:
            i += 1
        elif A[i+1] == 0:
            A[i+1], A[i+1+zeros] = A[i+1+zeros], 0
    return A


A = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7]
B = delete_dup_and_shift(A)
print(B)
