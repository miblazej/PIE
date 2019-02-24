import string


def sin_string(s):
    # rozdzielenie lancucha znakow na trzy
    dlugosc = len(s)
    s1, s2, s3 = '', '', ''
    for i in range(dlugosc):
        if (i - 1) % 4 == 0:
            s1 += s[i]
        elif i % 2 == 0:
            s2 += s[i]
        else:
            s3 += s[i]
    # napisanie wyrazow w odpowiedniej kolejnosci
    # konwersja wyrazow tak aby odpowiadaly
    s11 = ' '
    s22 = ''
    s33 = '   '
    for i in range(len(s1)):
        s11 += s1[i] + '   '
    for i in range(len(s2)):
        s22 += s2[i] + ' '
    for i in range(len(s3)):
        s33 += s3[i] + '   '
    print(s11 + '\n' + s22 + '\n' + s33)
    return True

s = 'Hello World!'
a = sin_string(s)
