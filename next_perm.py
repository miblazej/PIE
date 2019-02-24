def next_perm(A):
    # find k
    k = 1
    for i in range(len(A)):
        if A[- 1 - i] < A[-2 - i]:
            k += 1
        else:
            break
    k = len(A) - k - 1
    # find smallest
    index = k + 1
    for i in range(k+1, len(A)):
        if A[i] < A[index]:
            index = i
    # swap
    A[k], A[index] = A[index], A[k]
    # reverse the sequence after k
    k += 1
    for i in range(len(A[k:-1])//2):
        A[k + i], A[-1 - i] = A[-1 - i], A[k + i]
    return A
A = [1, 2, 4, 3, 0]
B = next_perm(A)
