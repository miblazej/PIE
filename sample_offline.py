import random


def sample_offline(A, size):
    subset = []
    while size:
        number = random.randint(0, len(A) - 1)
        subset.append(A.pop(number))
        size -= 1
    return subset
A = [1, 2, 3, 4, 5]
B = sample_offline(A, 3)
print(B)
