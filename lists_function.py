# plik zawierarający klase połączonej listy oraz podstawowe funckje pokrewne
# klasa ListNode


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

# funckja przeszukujaca liste w celu odnalezienia klucza


def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

# Funckja wpisujaca NodeList za kolejnym miejscem


def insert_list(ins_node, base_node):
    ins_node.next = base_node.next
    base_node.next = ins_node

# Funckja usuwająca NodeList z listy


def delete_after(node):
    node.next = node.next.next

# Funckja dodajaca element na koncu listy


def add_end(base_node, next_node):
    base_node.next = next_node


# algorytm tworzacy szereg dla listy
Head = ListNode(1)
last = ListNode(2)
add_end(Head, last)
for i in range(10):
    L2 = ListNode(i + 3)
    add_end(last, L2)
    last = L2

# Zadanie 7.1 Zakładając że dwie listy sa w uporządkowanym porządku
# stwórza lgorytm który połączy te listy tak aby nadal były w
# kolejnosci od najmniejszej do największej
# Deklaracja list

L1 = ListNode(1)
last = L1
for i in range(2, 10, 2):
    L2 = ListNode(i)
    add_end(last, L2)
    last = L2

L2 = ListNode(2)
last = L2
for i in range(3, 20, 4):
    L3 = ListNode(i)
    add_end(last, L3)
    last = L3
# Funckja scalająca obydwie listy


def merge_list(L1, L2):
    # petla przesuwajaca sie przez kolejne elementy listy L1 oraz sprawdzajaca czy
    # pierwszy element z L2 jest wiekszy od aktualnego elelemntu w L1
    head = L1
    tail = ListNode()
    while L1 and L2:
        if L1.data > L2.data:
            L1.data, L2.data = L2.data, L1.data
            L1.next, L2.next, L2 = L2, L1.next, L2.next
            tail = L1
        else:
            tail = L1
            L1 = L1.next


    # dodadnie ewentualnego uporzadkowanego konca lancucha
    if L2.next != None:
        tail.next = L2
    return head


# test
a = merge_list(L1, L2)



