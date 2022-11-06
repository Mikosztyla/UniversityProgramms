# Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.
import random
import math


def get_tab_length(tab):
    s = 0
    for i in tab:
        s += 1
    return s


def get_one_list(tab, n):
    tab_length = n
    count = 1
    while tab_length > 1:
        if tab_length % 2 == 1:
            multilist = [[-1 for _ in range(n * count * 2)] for _ in range((tab_length + 1)//2)]
            multilist[-1] = tab[-1]
        else:
            multilist = [[-1 for _ in range(n * count * 2)] for _ in range(tab_length//2)]

        for lists in range(0, tab_length-1, 2):
            i, j = 0, 0
            m_it = 0
            while i < get_tab_length(tab[lists]) and j < get_tab_length(tab[lists + 1]):
                if tab[lists][i] <= tab[lists + 1][j]:
                    multilist[lists // 2][m_it] = tab[lists][i]
                    m_it += 1
                    i += 1
                else:
                    multilist[lists // 2][m_it] = tab[lists + 1][j]
                    m_it += 1
                    j += 1
            for k in tab[lists][i:]:
                multilist[lists // 2][m_it] = k
                m_it += 1
            for k in tab[lists + 1][j:]:
                multilist[lists // 2][m_it] = k
                m_it += 1
        tab = multilist
        tab_length = math.ceil(tab_length/2)
        count *= 2
    return tab[0]


def singletony(tab):
    counter = 1
    it = 0
    result = [-1 for _ in range(get_tab_length(tab))]
    for i in range(get_tab_length(tab)-1):
        if tab[i] == -1:
            break
        if tab[i] == tab[i+1]:
            counter += 1
        else:
            if counter > 1:
                counter = 1
            else:
                result[it] = tab[i]
                it += 1
    s = 0
    for i in result:
        if i == -1:
            break
        s += 1
    result2 = [0 for _ in range(s)]
    for i in range(s):
        result2[i] = result[i]
    return result2


n = int(input("Podaj zakres: "))
tab = [[0 for _ in range(n)] for _ in range(n)]
m = 100
for i in range(n):
    tab[i][0] = random.randint(1, m)
    for j in range(1, n):
        if tab[i][j-1] == m:
            temp = m
        else:
            temp = random.randint(1, m)
            while temp < tab[i][j-1]:
                temp = random.randint(1, m)
        tab[i][j] = temp

for i in range(n):
    print(tab[i])
# tab = [[2,3,7], [2,3,4], [2,5,6]]
# n = len(tab)

print()
print(singletony(get_one_list(tab, n)))