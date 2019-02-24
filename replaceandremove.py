import pytest


def replace_and_remove(s, i):
    new = ''
    for a in range(len(s)):
        if s[a] == 'b':
            pass
        elif s[a] == 'a':
            new += 'dd'
        else:
            new += s[a]
    return new

s = 'baaaa'

replace_and_remove(s, 4)


def test_answer():
    d = replace_and_remove(s, 4)
    assert d == 'dddddddd'


