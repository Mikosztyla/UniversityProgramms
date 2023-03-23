# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


def print_forward(zb):
    while zb:
        print(zb.value, end=" ")
        zb = zb.next
    print()
    return


def print_backward(zb):
    if zb:
        print_backward(zb.next)
        print(zb.value, end=" ")
    print()
    return


def scal(p1, p2):
    if not p1 and not p2:
        return None
    if not p1:
        return p2
    if not p2:
        return p1

    q = Node()
    if p1.value < p2.value:
        q = p1
        p1 = p1.next
    else:
        q = p2
        p2 = p2.next

    res = q
    while p1 and p2:
        if p1.value < p2.value:
            q.next = p1
            p1 = p1.next
        else:
            q.next = p2
            p2 = p2.next
        q = q.next
    if p1:
        q.next = p1
    elif p2:
        q.next = p2
    return res


def scal_rec(p1, p2):
    if not p1 and not p2:
        return None
    q = Node()
    if p1.value < p2.value:
        q = p1
        p1 = p1.next
    else:
        q = p2
        p2 = p2.next

    def rec(q, p1, p2):
        if not p1:
            q.next = p2
            return q
        if not p2:
            q.next = p1
            return q
        if p1.value < p2.value:
            q.next = rec(p1, p1.next, p2)
        else:
            q.next = rec(p2, p1, p2.next)
        return q

    return rec(q, p1, p2)


p = Node()
p1 = p
l = Node(1)
p2 = l
for i in range(2, 20):
    if i % 2 == 0:
        k = Node(i)
        p.next = k
        p = k
    else:
        m = Node(i)
        l.next = m
        l = m

print_forward(p1)
print_forward(p2)
t = scal_rec(p1, p2)
print_forward(t)


