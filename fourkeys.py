def four_keys(A):
    # grupa 1 A[:g1]
    # grupa 2 A[g1:g2]
    # grupa 3 A[g2:g3]
    # grupa 4 A[g3:]
    G1 = A[0]
    G2, G3, G4 = 0, 0, 0
    g1, g2, g3 = 1, 1, 1
    # szukanie wartosc
    for i in range(len(A)):
        if A[i] != G1 and G2 == 0:
            G2 = A[i]
        elif A[i] != G1 and A[i] != G2 and G3 == 0:
            G3 = A[i]
        elif A[i] != G2 and A[i] != G3 and A[i] != G1 and G4 == 0:
            G4 = A[i]
            break
    # przypisywanie wartosci
    for i in range(1, len(A)):
        element = A.pop(i)
        if element == G1:
            A.insert(0, element)
            g1 += 1
            g2 += 1
            g3 += 1
        elif element == G2:
            A.insert(g1, element)
            g1 += 1
            g2 += 1
            g3 += 1
        elif element == G3:
            A.insert(g2, element)
            g2 += 1
            g3 += 1
        elif element == G4:
            A.insert(g3, element)
            g3 += 1
    return element

A = [1, 2, 3, 4, 2, 3, 4, 1, 2, 3, 4]
B = four_keys(A)
