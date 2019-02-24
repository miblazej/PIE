import string


def say_and_look(l, n):
    # zmienne pomocnicze
    liczba = 0
    wystapienia = 0
    s = str(l)
    new_s = ''
    # petla determinujaca ilosc iteracji funckji
    for i in range(n):
        if i > 0:
            s = '' + new_s
            new_s = ''
        for j in range(len(s)):
            if i == 0 and j == 0:
                new_s = str(1) + str(l)
            elif j == 0:
                liczba = s[0]
                wystapienia = 1
            elif s[j] == liczba:
                wystapienia += 1
            elif s[j] != liczba:
                new_s += str(wystapienia) + str(liczba)
                liczba = s[j]
                if j == len(s) - 1:
                    new_s += str(1) + str(liczba)
    return new_s

a = say_and_look(7, 8)
print(a)
