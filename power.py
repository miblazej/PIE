def potega(x, y):
    wynik = x
    if y < 0:
        x = 1 / x
        y = -y
    while y:
        if y & 0x1:
            wynik *= x
        x, y = x * x, (y >> 1)
    return wynik


a = potega_dodatnia(2, -10)
print(str(a))

# Michal Blazej
