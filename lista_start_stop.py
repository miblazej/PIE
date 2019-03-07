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
        sublista_iter.next, temp.next, start_zmiany.next = (temp.next, start_zmiany.next, temp)
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

a = odwrocListe(L1)
print(a)
