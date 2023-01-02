# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

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


def reverse(t):
    if not t:
        return None
    q = Node()
    q.value = t.value
    k = Node()
    t = t.next
    while t:
        k = Node(t.value)
        k.next = q
        q = k
        t = t.next
    return q


p = Node()
p1 = p
for i in range(2, 20):
    if i % 2 == 0:
        k = Node(i)
        p.next = k
        p = k
print_forward(p1)
p1 = reverse(p1)
print_forward(p1)