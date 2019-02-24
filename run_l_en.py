import string


# funkcja dekodujaca
def decoding(s):
    # funkcja dekodujaca stringa w postaci RLE
    numeryczne = ''
    a = ''
    for i in range(len(s)):
        # wyszukiwanie liczb numerycznych
        if s[i].isnumeric():
            numeryczne += s[i]
        else:
            for ii in range(int(numeryczne)):
                a += s[i]
            numeryczne = ''
    print(a)


def encoding(s):
    # funckja kodujaca do postaci RLE
    s1 = ''
    counter = 1
    for i in range(len(s) - 1):
        # zliczanie takich samych znakow
        if s[i] == s[i + 1]:
            counter += 1
        elif s[i] != s[i + 1]:
            s1 += str(counter) + s[i]
            counter = 1
        if s[i] == s[i + 1] and i == (len(s) - 2):
            s1 += str(counter) + s[i]
            counter = 1
        elif s[i] != s[i + 1] and i == (len(s) - 2):
            s1 += '1' + s[i + 1]
    return s1

S = 'aaaaaffffffffassssssssssab'
c = encoding(S)
print(c)
print(decoding(c))
