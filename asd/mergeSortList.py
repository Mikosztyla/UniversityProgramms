class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_list(l1, l2):
    if l1.value < l2.value:
        start = l1
        start_head = start
        l1 = l1.next
        start.next = None
    else:
        start = l2
        start_head = start
        l2 = l2.next
        start.next = None

    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            start.next = l1
            l1 = l1.next
        else:
            start.next = l2
            l2 = l2.next
        start = start.next
        start.next = None

    if l2 is None:
        start.next = l1
    else:
        start.next = l2

    return start_head


def seperate(p):
    if p is None or p.next is None:
        return p
    head = p
    s = p
    p = p.next
    while p and s.value < p.value:
        s = p
        p = p.next
    s.next = None
    return head, p


def merge_sort(l1):
    while True:
        l2 = None
        tail = l2
        cnt = 0
        while l1 is not None:
            block1, l1 = seperate(l1)
            block2, l1 = seperate(l1)
            tail.next = merge_list(block1, block2)
            while tail.next is not None:
                tail = tail.next
            cnt += 1
        if cnt == 1:
            return l2
        l1 = l2


def tab_to_list(tab):
    p = Node(tab[0])
    k = p
    for i in range(1, len(tab), 1):
        k.next = Node(tab[i])
        k = k.next
    return p


def print_list(p):
    while p:
        print(p.value, end=" ")
        p = p.next
    print()


tab = [1, 4, 6, 3, 4, 8, 9]
p = tab_to_list(tab)
print_list(p)
a, b = seperate(p)
print_list(a)
print_list(b)
p = merge_list(a, b)
print_list(p)