import numpy as np


def coin():
    a = np.random.randint(2)
    return a


def random_generator(a, b):  # gauusian distribution
    przedzial = b - a
    przedzial_t = przedzial
    bits = 0
    # calculation of numbers of bit required to represent przedzial
    while przedzial:
        przedzial >>= 1
        bits += 1
    while 1:
        number = 0
        temp = bits
        while temp:
            c = coin()
            number <<= 1
            number ^= c
            temp -= 1
        if number <= przedzial_t:
            break
    return number + a

d = []
for i in range(100):
    d.append(random_generator(0, 100))
print('a')
