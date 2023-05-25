def heapify(tab, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_i = i
    if l < n and tab[max_i] < tab[l]:
        max_i = l
    if r < n and tab[max_i] < tab[r]:
        max_i = r

    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def build_heap(tab, n):
    for i in range((n-2)//2, -1, -1):
        heapify(tab, i, n)


def heap_sort(tab):
    n = len(tab)
    build_heap(tab, n)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)


T = [3, 7, 8, 2, 4, 34, 12, 78, 6, 9]
heap_sort(T)
print(T)