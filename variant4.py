def variant4(A):
    # Space: O(1)
    # Time : O(N)
    # Function description: Function that sorts boolean arrays without relative
    # of True values at the end of the array
    i = 0
    stop = len(A)
    while i < stop:
        if A[i]:
            A.append(A.pop(i))
            stop -= 1
            i -= 1
        i += 1
    return A

A = [True, False, True, False, True, False, True, True, False]
B = variant4(A)
print(B)
