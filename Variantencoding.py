def Sum(A, B):
    # Aditional space: O(1)
    # Time complexity: O(n)
    # Inputs: Arrays A and B with 0 and 1 values
    # Output: String of bits representing number A + B in encoded version
    sum = 0
    end_index = len(A)
    power = 0
    C = []
    for i in range(end_index-1, -1, -1):
        sum += A[i] * (2 ** power)
        power += 1
    end_index = len(B)
    for i in range(end_index-1, -1, -1):
        sum += B[i] * (2 ** power)
    while sum:
        if sum & 0x1:
            C.insert(0, 1)
        else:
            C.insert(0, 0)
        sum >>= 1
    return C

A = [1, 0, 1, 0, 1, 1]
B = [1, 0, 0, 0, 0, 0]
C = Sum(A, B)
