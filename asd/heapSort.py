def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(tab, i, n):
    l = left(i)
    r = right(i)
    max_i = i
    if l < n and tab[l] > tab[max_i]:
        max_i = l
    if r < n and tab[r] > tab[max_i]:
        max_i = r

    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def build_heap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)


def heap_sort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)


tab = [6, 4, 8, 3, 1, 9, 5, 3, 7, 5, 4]
heap_sort(tab)
print(tab)