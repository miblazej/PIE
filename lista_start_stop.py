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
    
    
    
    return glowa


L1 = ListNode(1)
last = L1
for i in range(2, 10, 2):
    L2 = ListNode(i)
    add_end(last, L2)
    last = L2
