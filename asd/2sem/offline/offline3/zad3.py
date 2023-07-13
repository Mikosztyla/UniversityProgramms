# Mikołaj Gosztyła
# Mój program na samym początku przechodzi po wszystkich wyrazach w tablicy i odwraca te wyrazy, których ostatnia
# litera ma mniejszą wartość w tabeli ASCII niż pierwsza. Następnie dzieli wyrazy względem ich długości i sortuje każdą
# grupę wyrazów o tej samej długości radix sortem. Ostatecznie przechodzi po całej tablicy posortowanych wyrazów
# zliczając największą ilość takich samych wyrazów.
from zad3testy import runtests


def counting_sort(tab, k):
    tab2 = [0 for _ in range(len(tab))]
    values = [0 for _ in range(27)]
    for el in tab:
        if len(el) < k:
            values[0] += 1
        else:
            values[ord(el[len(el)-k]) - 96] += 1
    for i in range(1, 27):
        values[i] += values[i-1]
    for i in range(len(tab)-1, -1, -1):
        if len(tab[i]) < k:
            values[0] -= 1
            tab2[values[0]] = tab[i]
        else:
            a = ord(tab[i][len(tab[i])-k]) - 96
            values[ord(tab[i][len(tab[i])-k]) - 96] -= 1
            tab2[values[ord(tab[i][len(tab[i])-k]) - 96]] = tab[i]
    return tab2


def strong_string(T):
    n = len(T)
    max_len = 0
    for el in T:
        if len(el) > max_len:
            max_len = len(el)
    lengths = [[] for _ in range(max_len)]
    for i in range(n):
        if T[i][0] > T[i][-1]:
            T[i] = T[i][::-1]
        lengths[len(T[i])-1] += [T[i]]
    T2 = []
    for i in range(max_len):
        if lengths[i]:
            for j in range(i+1):
                lengths[i] = counting_sort(lengths[i], j+1)
            T2 += lengths[i]
    T = T2
    max_result = 1
    curr_result = 1
    for i in range(1, n, 1):
        if T[i] == T[i-1]:
            curr_result += 1
        else:
            max_result = max(max_result, curr_result)
            curr_result = 1
    max_result = max(max_result, curr_result)
    return max(max_result, curr_result)


runtests( strong_string, all_tests=True )
