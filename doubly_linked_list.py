# Solve the same problem with doubly linked lists


class PListCzlon:
    def __init__(self, wartosc=0, nastepny=None, poprzedni=None):
        self.wartosc = wartosc
        self.nastepny = nastepny
        self.poprzedni = poprzedni

#function that adds next argument to doubly linked lists


def dodaj_element(podstawa, nastepny):
    podstawa.nastepny = nastepny
    nastepny.poprzedni = podstawa

# generation of first list
glowa = ostatni = PListCzlon(1)
for i in range(2,20,3):
    L1 = PListCzlon(i)
    dodaj_element(ostatni,L1)
    ostatni = L1
L1 = glowa

# generation of second list
glowa = ostatni = PListCzlon(-12)
for i in range(-10,40,8):
    L2 = PListCzlon(i)
    dodaj_element(ostatni,L2)
    ostatni = L2
L2 = glowa

# function that merges doubly linked list, list have to be in appending order
def P_zespolenie(L1, L2):
    # Create first node
    glowa = ostatni = PListCzlon()
    while L1 and L2:
        if L1.wartosc > L2.wartosc:
            L2.poprzedni = ostatni
            ostatni.nastepny, L2 = L2, L2.nastepny
        else:
            L1.poprzedni = ostatni
            ostatni.nastepny, L1 = L1, L1.nastepny
        ostatni = ostatni.nastepny
    # podlączenie pozostałości która jest już posortowana
    if L1 is not None:
        L1.poprzedni = ostatni
        ostatni.nastepny = L1
    else:
        L2.poprzedni = ostatni
        ostatni.nastepny = L2
    return glowa

a = P_zespolenie(L1,L2)






