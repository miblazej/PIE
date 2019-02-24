import string


# deklaracja klawiszologi
KLAWISZE = (
    '0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def mnemonics(number):
    def phone_mnemonic_helper(digit):
        if digit == len(number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for znak in KLAWISZE[int(number[digit])]:
                partial_mnemonic[digit] = znak
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(number)
    phone_mnemonic_helper(0)
    return mnemonics

numer = '8592708'
mn = mnemonics(numer)

# rozwiaz ten sam problem bez uzycia rekursywnosci
def permutacja(numer):
    