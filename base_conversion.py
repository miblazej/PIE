import functools
import string


def base_covert(number, b1, b2):
    # int convertion
    liczba = int(number)
    is_negative = False
    if liczba < 0:
        is_negative = True
        liczba = abs(liczba)
    b1 = int(b1)
    b2 = int(b2)
    base10 = 0
    power = 0
    # convertion to decimal system
    while liczba:
        base10 += (liczba % 10) * b1 ** power
        liczba //= 10
        power += 1
    # convertion to b2
    # max digit
    power = 0
    while b2 * b2 ** power < base10:
        power += 1
    number = ''
    # maksymalna mozliwa liczba w systemie opartym na b2
    while base10 != 0:
        a = 0
        b = 0
        # sprawdzenie mozliwosci
        while a < b2:
            b = a * (b2 ** power)
            if b > base10:
                a -= 1
                b = a * (b2 ** power)
                break
            a += 1
        power -= 1
        base10 -= b
        if a < 10:
            number += str(a)
        else:
            number += (chr(ord('A') + a % 10))
    return ('-' if is_negative else '') + ''.join(number)


def base_convertion_faster(number, b1, b2):
        # int convertion
    liczba = int(number)
    is_negative = False
    if liczba < 0:
        is_negative = True
        liczba = abs(liczba)
    b1 = int(b1)
    b2 = int(b2)
    base10 = 0
    power = 0
    # convertion to decimal system
    while liczba:
        base10 += (liczba % 10) * b1 ** power
        liczba //= 10
        power += 1
    # convertion to new system with modulo operation
    baseb2 = ''
    while base10:
        a = base10 % b2
        base10 = base10 // b2
        if a < 10:
            baseb2 += str(a)
        else:
            baseb2 += (chr(ord('A') + a % 10))
    if is_negative:
        baseb2 += '-'
    base = baseb2[::-1]
    return base

number = '-42154431'
b1 = 5
b2 = 14
nowa = base_convertion_faster(number, b1, b2)
print(nowa)
