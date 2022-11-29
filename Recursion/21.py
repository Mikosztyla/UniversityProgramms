# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
import random
def fill_row(i, tab):
    for k in range(8):
        tab[i][k] = True


def fill_col(j, tab):
    for k in range(8):
        tab[k][j] = True


# def fill_diagonal(i, j, tab):
#     m = 0
#     i_mem = i
#     j_mem = j
#     while i >= 0 and j >= 0:
#         tab[i][j] = True
#         i -= 1
#         j -= 1
#     i = i_mem
#     j = j_mem
#     while i >= 0 and j <= 7:
#         tab[i][j] = True
#         i -= 1
#         j += 1
#     i = i_mem
#     j = j_mem
#     while i <= 7 and j >= 0:
#         tab[i][j] = True
#         i += 1
#         j -= 1
#     i = i_mem
#     j = j_mem
#     while i <= 7 and j <= 7:
#         tab[i][j] = True
#         i += 1
#         j += 1


def fill_tab(tab, x, y):
    fill_row(x, tab)
    fill_col(y, tab)
    #fill_diagonal(x, y, tab)


def rem_tab(tab, mem_tab):
    for m in range(8):
        for l in range(8):
            mem_tab[m][l] = tab[m][l]


def sumy(T, tab, suma, p=0):
    if p < 8:
        for i in range(p, 8):
            for j in range(8):
                if not tab[i][j]:
                    mem_tab = [[False for _ in range(8)] for _ in range(8)]
                    rem_tab(tab, mem_tab)
                    fill_tab(tab, i, j)
                    if suma == T[i][j]:
                        print(T[i][j], i, j)
                        return True
                    if suma - T[i][j] > 0:
                        if sumy(T, tab, suma - T[i][j], i+1):
                            print(T[i][j], i, j)
                            return True
                    rem_tab(mem_tab, tab)
    return False


tab = [[False for _ in range(8)] for _ in range(8)]
#T = [[random.randint(1, 9) for _ in range(8)] for _ in range(8)]
T = [
[5, 5, 2, 2, 5, 9, 2, 4],
[2, 2, 1, 8, 8, 2, 6, 4],
[4, 2, 2, 7, 8, 2, 5, 8],
[3, 5, 2, 1, 7, 8, 3, 6],
[7, 9, 9, 5, 7, 8, 3, 8],
[2, 3, 3, 6, 4, 3, 6, 5],
[4, 7, 6, 1, 4, 6, 6, 6],
[3, 2, 7, 6, 3, 4, 8, 2]
]
for i in range(8):
    print(T[i])
print(sumy(T, tab, 40))