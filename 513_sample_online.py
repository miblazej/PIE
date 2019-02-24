import random
import operator


def random_permutation(n):
    perm = []
    lista = [x for x in range(0, n)]
    for i in range(n):
        perm.append(lista.pop(random.randint(0, n - i - 1)))
    return perm

permuation = random_permutation(10)
print(permuation)
lista_kumulacyjna = [0 for x in range(10)]
for i in range(1000):
    permuation = random_permutation(10)
    for a in range(10):
        lista_kumulacyjna[a] += permuation[a]
print(lista_kumulacyjna)
