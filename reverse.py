def odwrotnie(x):
    x_str = str(x)
    d = len(x_str)
    odw = []
    for i in range(d):
        odw.append(x_str[d - i - 1])
    odw = ''.join(odw)
    return int(odw)

o = odwrotnie(123)
print(str(o))


def odw_modulo(x):
    minus = 1
    wynik = 0
    if x < 0:
        x = - x
        minus = -1
    while x:
        wynik *= 10
        wynik += (x % 10)
        x -= (x % 10)
        x /= 10
    return wynik * minus

print(str(odw_modulo(-215)))

# Michal Blazej
