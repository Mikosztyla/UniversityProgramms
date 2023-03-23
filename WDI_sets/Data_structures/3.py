# Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę
# napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji
# należy przekazać położenie hetmanów.

def fill_row(T, i, tab):
    for k in range(10):
        tab[i][k] += 1


def fill_col(T, j, tab):
    for k in range(10):
        tab[k][j] += 1


def fill_diagonal(T, i, j, tab):
    m = 0
    i_mem = i
    j_mem = j
    while i >= 0 and j >= 0:
        tab[i][j] += 1
        i -= 1
        j -= 1
    i = i_mem
    j = j_mem
    while i >= 0 and j <= 9:
        tab[i][j] += 1
        i -= 1
        j += 1
    i = i_mem
    j = j_mem
    while i <= 9 and j >= 0:
        tab[i][j] += 1
        i += 1
        j -= 1
    i = i_mem
    j = j_mem
    while i <= 9 and j <= 9:
        tab[i][j] += 1
        i += 1
        j += 1


def check_T(T, tab):
    for el in T:
        x, y = el
        if tab[x][y] > 0:
            return False
    return True


T = [(3, 5), (1, 2), (4, 5), (8, 9)]
n = len(T)
tab = [[0 for _ in range(10)] for _ in range(10)]
for el in T:
    x, y = el
    fill_row(T, x, tab)
    fill_col(T, y, tab)
    fill_diagonal(T, x, y, tab)
    tab[x][y] -= 6


# tab_test = [[j+i for i in range(10)] for j in range(10)]
# for i in range(10):
#     print(tab_test[i])

for i in range(10):
    print(tab[i])
print()
print(check_T(T, tab))
