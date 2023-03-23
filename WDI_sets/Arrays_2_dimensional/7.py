# Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.
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

    s = 0
    for i in tab[0]:
        if i == -1:
            break
        s += 1
    result = [0 for _ in range(s)]
    for i in range(s):
        result[i] = tab[0][i]

    return result


n = int(input("Podaj zakres: "))
tab = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tab[i][0] = random.randint(1, 20)
    for j in range(1, n):
        if tab[i][j-1] == 20:
            temp = 20
        else:
            temp = random.randint(1, 20)
            while temp < tab[i][j-1]:
                temp = random.randint(1, 20)
        tab[i][j] = temp

for i in range(n):
    print(tab[i])
# tab = [[2,3,7], [2,3,4], [2,5,6]]
# n = len(tab)

print()
print(get_one_list(tab, n))