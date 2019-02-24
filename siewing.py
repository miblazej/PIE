def sew(n):
    pierwsze = []
    sito = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if sito[p]:
            pierwsze.append(p)
            for i in range(p, n + 1, p):
                sito[i] = False
    return pierwsze
A = sew(132)
print(A)
