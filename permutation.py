def permutation(A, permutation_array):
    B = [0] * len(A)
    for i in range(len(A)):
        B[permutation_array[i]] = A[i]
    return B

A = ['a', 'b', 'c', 'd']
P = [3, 2, 1, 0]
B = permutation(A, P)
print(B)
