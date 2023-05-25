import random


def partition(tab, l, p):
    x = tab[p]
    i = l
    for j in range(l, p):
        if tab[j] < x:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    tab[i], tab[p] = tab[p], tab[i]
    return i


def quick_sort(tab, l, p):
    if l < p:
        q = partition(tab, l, p)
        quick_sort(tab, l, q-1)
        quick_sort(tab, q+1, p)


tab = [random.randint(1, 100) for _ in range(20)]
quick_sort(tab, 0, len(tab)-1)
print(tab)
