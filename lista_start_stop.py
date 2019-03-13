from list1 import ListNode
from lists_function import add_end

# Funckja przyjmujaca trzy elementy :
# Pierwszy czlon listy
# start oraz stop, elementy listy od start do stop wlacznie powinny miec zamieniona kolejnosc
# pierwszy element czlonu listy ma indeks jeden zakladam ze glowa nie jest pustym elementem


def odwrocSubListe(glowa, start, stop):
    # stworzenie czlonow listy majacych przechowac wskazniki do pierwszego czlonu
    # zamiany oraz ostatniego czlonu zamiany
    # do zrobienia jutro
    start_zmiany = ListNode(0, glowa)
    for _ in range(1, start):
        start_zmiany = start_zmiany.next
    # w tym momencie start_zmiany jest poczatkiem którą mam odwrócić
    # proces odwrocenia listy
    sublista_iter = start_zmiany.next
    for _ in range(stop - start):
        temp = sublista_iter.next
        sublista_iter.next, temp.next, start_zmiany.next = (
            temp.next, start_zmiany.next, temp)
    return glowa.next


def odwrocListe(glowa):
    pre = glowa
    glowa = glowa.next
    pre.next = None
    while(1):
        pre, glowa.next, glowa = (glowa, pre, glowa.next)
        if (glowa.next is None):
            break
    glowa.next = pre
    return glowa


L1 = ListNode(1)
last = L1
for i in range(2, 10, 2):
    L2 = ListNode(i)
    add_end(last, L2)
    last = L2

# napisz program ktory zabieraj jako imput pojedynczo polaczona liste oraz nie niegatywne
# liczby typu int k oraz odwraca wtedy k czesci. Jezeli liczba czlonow n w liscie nie jest
# mnoznikiem liczby k zostaw ostatnie n modulo k czlonow niezmienionych. Nie zmieniaj wartosci
# ktore sa zapisane w czlonach


def coenty(L1, k):
    if (k < 1):
        return L1
    elif (k == 1):
        return odwrocListe(L1)
    # caly proces wydaje sie byc troche niejasny dla mnie z powodu braku swojej uzytecznosci
    # mimo tego opracowalem algorytm polegajacy na zmianie wskaznika w co k-tym elemencie
    # co w rezultacie skutkuje zamiana miejsc w szeregu listy na pozycjach k orz k-1
    # w zwiazku z dowolnym k podanym na wejscu funkcji potrzebny jest licznik resetujacy sie
    # po kazdej operacji zamiany potrzebna bedzie zmiana wartosci czterech zmiennych
    # 1. wskaznik na element k-1 ma wskazywac na element k
    # 2. wskaznik na element k+1 ma wskazywc na element k-1
    # 3. wskaznik na element k ma wskazywac na element k+1
    # deklaracja zmiennej licznik
    licznik = 2
    # przeprowdzanie operacji opisanych wczesniej sa potrzebne
    # 1. pre_2 - obiekt ktorego pole next nalezy zmienic w przypadku licznikia == k
    # 2. prze - obiekt ktorego pole next nalezy zmienic w przypadku licznika == k
    # 3. aktualny - obiekt ktorego pole next nalezy zmienic w przypadku licnzika == k
    while(L1.next is not None):
        if (licznik == k):
            n = L1.next
            nn = L1.next.next
            nnn = L1.next.next.next
            nn.next = n  # wskaznik z elementu o indeksie 2 wskazuje na drugi element
            n.next = nnn    # wskaznik z elementu o indeksie 1 wskazuje na czwarty element
            L1 = nnn  # zmiana aktualnej pozycji okna na pierwszy element nastepujacy po zmianie indeksow
            licznik = 1  # potrzebne aby zachowac odstepy o szerokosci k
        else:
            # update licznika oraz update zmiennej L1
            licznik += 1
            L1 = L1.next
    return L1


coenty(L1, 2)
