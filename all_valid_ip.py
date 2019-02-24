import string


def adresy_ip(s):
    # funckja ktora drukuje wszystkie mozliwe adresy ip stworzone
    # z stringa o dlugosci od 4 do 12
    # adres ip sklada sie z czterech sub adresow ktore moga przyjac
    # wartosci od 0 do 255(8 bit)
    # spradzenie poprawnosci danych wejsciowych
    if len(s) >= 4 and len(s) <= 12:
        pass
    else:
        print('Niepoprane dane wejsciowe')
        return False
    # algorytm szukajacy oraz sprawdzajacy poprawnosc adresow ip
    a1, a2, a3, a4 = '', '', '', ''
    k = len(s)
    # brutalne wykorzystanie mocy obliczeniowej
    for o1 in range(1, 4):
        a1 = ''
        a1 = s[0:o1]
        if int(a1) < 256:
            for o2 in range(o1 + 1, o1 + 4):
                # sprawdzenie czy o2 nie wyszedl poza indeks
                if o2 + 1 >= k:
                    break
                a2 = ''
                a2 = s[o1:o2]
                if int(a2) < 256:
                    for o3 in range(o2 + 1, o2 + 4):
                        if o3 == k:
                            break
                        a3 = ''
                        a4 = ''
                        a3 = s[o2:o3]
                        a4 = s[o3:k]
                        if int(a3) < 256:
                            if int(a4) < 256:
                                print(a1 + '.' + a2 + '.' + a3 + '.' + a4)
    return False

s = '123123123123'
a = adresy_ip(s)
# zadanie rozwiazano poprawnie