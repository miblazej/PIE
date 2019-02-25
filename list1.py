# linked list exercises

class ListNode:
    def __init__(self, data=0, next_node = None):

        self.data = data

        self.next = next_node
        return

def merge_lists(L1, L2):
    # stworzyc pierwszy element listy
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1 < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next
    # kod zostal przepisany z ksiazki nie wymyslilem tego

    





    


