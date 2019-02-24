def alternation(A):
    # program that computes alternation b0 <= b1 >= b2 <= b3 >= b4
    # and so on until the end of array
    # first sort A array
    A = sorted(A)
    d = len(A) // 2
    B = []
    if d & 0x1:
        i = 0
        while i < d:
            B.append(A[i])
            B.append(A[-1 - i])
            i += 1
        B.append(A[i])
    else:
        i = 0
        while i <= d:
            B.append(A[i])
            B.append(A[-1 - i])
            i += 1
    return B

A = [1, 2, 4, 3, 5, 1, 4, 2, 6, 3]
B = alternation(A)
print(B)
