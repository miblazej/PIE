import functools


# program do kowersji systemu rzymsiego na arabski
def convroman2arab(s):
    # slownik z wartosciami
    wartosc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    suma = 0
    # sumacja wszystkich znakow
    for i in range(len(s)):
        suma += wartosc[s[i]]
        # exceptions
        if (i > 0 and s[i - 1] == 'I') and (s[i] == 'V' or s[i] == 'X'):
            suma -= 2
        elif (i > 0 and s[i - 1] == 'X') and (s[i] == 'L' or s[i] == 'C'):
            suma -= 20
        elif (i > 0 and s[i - 1] == 'C') and (s[i] == 'D' or s[i] == 'M'):
            suma -= 200
    return suma

znak = 'MDIX'
war = convroman2arab(znak)
print(war)
z = [10, 10, 10, 12, - 100, - 200]
d = functools.reduce(lambda x, y: x - y, z)
print(d)


# program do sprawdzenia poprawnosci liczby rzymskiej
def check_roman(s):
    for i in range(2, len):
        if (s[i - 2] == 'I' and s[i - 1] == 'I') and (s[i] == 'V' or s[i] == 'X'):
            return False
        elif (s[i - 2] == 'X' and s[i - 1] == 'X') and (s[i] == 'L' or s[i] == 'C'):
            return False
        elif (s[i - 2] == 'c' and s[i - 1] == 'C') and (s[i] == 'D' or s[i] == 'M'):
            return False
    return True


# program do sporządzenia najkrótszej liczby rzymksiej bedącej odpowiednikiem
def arab_to_roman(i):
    # tablica z wartosciami
    wartosc = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
               'XC': 90, 'L': 50, 'XL': 40,
               'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    s = ''
    while i:
        for key, value in wartosc.items():
            if (i - value) >= 0:
                i -= value
                s += key
                break
    return s
s = arab_to_roman(1509)
print(s)
