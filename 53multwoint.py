def strmul(A, B):
    # Time complexity : O(n^2)
    # Additional space O(n)
    # Input : two strings with integer numbers written in string
    # Output: Result of multiplication of those numbers
    # Calculation of output sign
    sign = 1
    if A[0] < 0 and B[0] > 0 or B[0] < 0 and A[0] > 0:
        sign = (-1)
    A[0] = abs(A[0])
    B[0] = abs(B[0])
    sum = [0 for i in range(len(A) + len(B))]
    index = len(A) + len(B)
    counter = 0
    a_len = len(A) - 1
    b_len = len(B) - 1
    for b in range(len(B)):
        if B[b_len - b]:
            for a in range(len(A)):
                calc_var = B[b_len - b] * A[a_len - a] + counter
                counter = calc_var // 10
                sum_index = index - b - a - 1
                sum_update = sum[sum_index] + calc_var % 10
                if sum_update >= 10:
                    sum_update = sum_update % 10
                    counter += 1
                sum[sum_index] = sum_update
            if counter:
                sum[sum_index - 1] += counter
                counter = 0
    i = 0
    while sum[i] == 0:
        i += 1
    del sum[0:i]
    sum[0] *= sign
    return sum

A = [-9, 9, 9]
B = [-9, 9, 9]
C = strmul(A, B)
print(C)
