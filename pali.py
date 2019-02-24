import pytest
import string


def pali(s):
    s1 = ''
    s2 = ''
    # petla while ktora skanuje kolejne elementy obiektu string i za tym samym
    # sprawdza warunek takich samych elementów na kazdym z koncow wyrazow
    # w petli while sa umieszczone dwie kolejne pętle while ktore sprawdzaja
    # czy znaki sa alpha numeryczne
    # zajmplementowane zmienne
    s1_index = 0
    s2_index = len(s) - 1
    while s1_index <= s2_index:
        # zapewnienie ze zaden znak alphanumeryczny nie zostal pominiety oraz
        while not s[s1_index].isalpha():
            s1_index += 1
        s1 = s[s1_index]
        while not s[s2_index].isalpha():
            s2_index -= 1
        s2 = s[s2_index]
        if s1 != s2:
            return False
        else:
            s1_index += 1
            s2_index -= 1
    return True


a = 'A,,,,,,,,,bb,A'
b = pali(a)


def test_():
    d = pali('Adupa')
    assert d == False
    assert pali('A,,,,b,,,,,,,,b,,,,,,,,A') == True
