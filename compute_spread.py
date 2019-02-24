import pytest


def base26tobase10(s):
    s = s[::-1]
    base10 = 0
    power = 0
    for i in range(len(s)):
        base10 += (ord(s[i]) - 64) * 26 ** power
        power += 1
    return base10

b = base26tobase10('AAAAAA')
print(b)


def base10tobase26(i):
    a = ''
    power = 0
    while i:
        c = i % 26
        if c == 0:
            a += 'Z'
            i -= 26 * 26 ** power
        else:
            a += chr(64 + c)
            i //= 26
        power += 1
    a = a[::-1]
    return a


def test_answer():
    assert base10tobase26(702) == 'ZZ'
test_answer()
