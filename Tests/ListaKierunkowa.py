class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    a = 5
    while a < x**0.5 + 1:
        if x % a == 0:
            return False
        a += 2
        if x % 2 == 0:
            return False
        a += 4
    return True


def print_list(w):
    while w:
        print(w.value, end=" ")
        w = w.next
    print()


def insert(el, zb):
    q = None
    r = zb
    while r and r.value < el:
        q = r
        r = r.next
    if not q and not r or (r and r.value == el):
        return zb
    w = Node(el)
    w.next = r
    if q:
        q.next = w
    else:
        zb = w
    return zb


def remove(el, zb):
    if not zb:
        return zb
    q = None
    r = zb
    while r and r.value < el:
        q = r
        r = r.next
    if not r:
        return zb
    if r.value == el:
        if q:
            q.next = r.next
        else:
            zb = r.next
    return zb


p = Node(2)
zb = p
for i in range(p.value+1, 30):
    if is_prime(i):
        k = Node(i)
        p.next = k
        p = k

print_list(zb)
zb = insert(6, zb)
print_list(zb)
zb = remove(13, zb)
print_list(zb)

