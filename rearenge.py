def rearange(A):
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
    return A
