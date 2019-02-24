def addone(A):
    # Additional space O(1)
    # Computation time O(n)
    # Desc. Function is treating numbers in array as parts of one big
    # decimal integer function is adding one to the number.
    end_index = len(A)
    # overload counter
    D = 1
    for i in range(end_index-1, -1, -1):
        if D + A[i] >= 10:
            A[i] = 0
            D = 1
        else:
            A[i] += D
            D = 0
    if A[0] == 0:
        A.insert(0, 1)  
    return A

A = [9, 9, 9, 9, 9, 9]
B = addone(A)
print(B)
