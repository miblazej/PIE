import math


def primes(a):
    # simplest way to calculate :
    A = []
    flag = 0
    A.append(2)
    for i in range(3, a, 2):
        flag = 1
        for j in range(len(A)):
            if i > math.sqrt(i):
                break
            if i % A[j] == 0:
                flag = 0
                break
        if flag:
            A.append(i)
    return A
A = primes(132)
print(A)
