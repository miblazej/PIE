def variant1(A):
    # function that finds the lenght of longes equal subset
    # T:O(n), S :O(n)
    longest = 0
    current = 1
    past = A[0]
    for i in range(1, len(A)):
        if past == A[i]:
            current += 1
            past = A[i]
        elif past != A[i]:
            current = 1
            past = A[i]
        if current > longest:
            longest = current
    return longest

A = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
d = variant1(A)
print(d)
