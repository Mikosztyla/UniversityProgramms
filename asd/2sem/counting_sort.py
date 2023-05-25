def counting_sort(tab):
    values = [0 for _ in range(10)]
    tab2 = [0 for _ in range(len(tab))]
    for el in tab:
        values[el] += 1
    for i in range(1, 10):
        values[i] += values[i-1]
    for i in range(len(tab)-1, -1, -1):
        values[tab[i]] -= 1
        tab2[values[tab[i]]] = tab[i]
    return tab2


tab = [2, 3, 2, 3, 2, 3]
tab = counting_sort(tab)
print(tab)