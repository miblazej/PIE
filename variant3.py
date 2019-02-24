def bools_array(A):
    # input is a boolean array order it so false are in the front with O(1)
    # additional space and O(N) time
    i = 0
    j = 0
    while i < len(A) and j < len(A):
        if A[i]:
            A.append(A.pop(i))
            i -= 1
        i += 1
        j += 1
    return A

A = [True, False, True, False, True, False, True, True, False]
B = bools_array(A)
print(B)
