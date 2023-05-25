import math


def get_digit(x, i):
    a = (x % (10**i)) // (10**(i-1))
    return a


def counting_sort(tab, k):
    tab2 = [0 for _ in range(len(tab))]
    values = [0 for _ in range(11)]
    for el in tab:
        if el < 10**(k-1):
            values[0] += 1
        else:
            values[get_digit(el, k) + 1] += 1
    for i in range(1, 11):
        values[i] += values[i-1]
    for i in range(len(tab)-1, -1, -1):
        if tab[i] < 10 ** (k - 1):
            values[0] -= 1
            tab2[values[0]] = tab[i]
        else:
            values[get_digit(tab[i], k) + 1] -= 1
            tab2[values[get_digit(tab[i], k) + 1]] = tab[i]
    return tab2


def radix_sort(tab):
    max_num = 0
    for el in tab:
        if el > max_num:
            max_num = el
    l = int(math.log(max_num, 10)) + 1
    for i in range(l):
        tab = counting_sort(tab, i+1)
    return tab


tab = [2, 6, 8, 23, 5, 456, 7564, 234, 99, 45, 76, 23424, 6556, 5445, 2331]
tab = radix_sort(tab)
print(tab)