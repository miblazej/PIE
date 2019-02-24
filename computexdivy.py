def xdivy_bruteforce(x, y):
    quotien = 0
    while x > y:
        x -= y
        quotien += 1
    return quotien


def xdiv_optimal(x, y):
    potega = 32
    wynik = 0
    while x > y:
        y_potega = y << potega
        while(x >= y_potega):
            wynik += (1 << potega)
            x -= y_potega
        potega -= 1
    return wynik

q = xdiv_optimal(1231231234171, 71)
print(str(q))
# Michal Blazej
