import random


class Node():
    def __init__(self, value, next = None):
        self.next = next
        self.value = value


def tab_to_list(tab):
    p = Node(tab[0])
    k = p
    for i in range(1, len(tab)):
        k.next = Node(tab[i])
        k = k.next
    return p


def partition(p, start, end, n):
    rem_p = p
    cnt = 0
    last = 0
    while cnt < end:
        if cnt == start:
            i = p
        p = p.next
        cnt += 1
    last = p
    j = i
    p = rem_p
    cnt = start
    i.value, last.value = last.value, i.value
    x = last.value
    midd = start
    i_shadow = p
    while j and cnt < n:
        if j.value < x:
            i.value, j.value = j.value, i.value
            i_shadow = i
            i = i.next
            midd += 1
        j = j.next
        cnt += 1
    last.value, i.value = i.value, last.value
    return midd


def quick_sort(p, start, end, n):
    if start < end:
        q = partition(p, start, end, n)
        quick_sort(p, start, q-1, n)
        quick_sort(p, q+1, end, n)


n = 20
tab = [random.randint(1, 100) for _ in range(n)]
# tab = [2, 5, 3, 1, 4]
p = tab_to_list(tab)
quick_sort(p, 0, len(tab)-1, len(tab))
for i in range(n):
    print(p.value)
    p = p.next