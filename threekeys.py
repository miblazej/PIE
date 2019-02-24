def threekeys(A):
    mi = min(A)
    ma = max(A)
    for i in range(len(A)):
        if A[i] < ma and A[i] > mi:
            pivot = A[i]
    table = []
    table.append(pivot)
    granical = 0
    granicap = 1
    for i in range(len(A)-1):
        if A[i] > pivot:
            table.insert(granicap, A[i])
        elif A[i] == pivot:
            table.insert(granical, A[i])
            granicap += 1
        else:
            table.insert(granical, A[i])
            granical += 1
            granicap += 1
    return table


A = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
B = threekeys(A)
print('a')
# Michal Blazej
