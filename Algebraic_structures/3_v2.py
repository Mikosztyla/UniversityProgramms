# Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę
# napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji
# należy przekazać położenie hetmanów.


def check_tab(tab):
    tab.sort()
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            return False
    return True


def result(rows, cols, diagonal1, diagonal2):
    if check_tab(rows) and check_tab(cols) and check_tab(diagonal1) and check_tab(diagonal2):
        return True
    return False


T = [(0, 0), (2, 1), (4, 4)]
n = len(T)
rows = [0 for _ in range(n)]
cols = [0 for _ in range(n)]
diagonal1 = [0 for _ in range(n)]
diagonal2 = [0 for _ in range(n)]
for i in range(n):
    x, y = T[i]
    rows[i] = x
    cols[i] = y
    diagonal1[i] = x-y
    diagonal2[i] = x+y

print(result(rows, cols, diagonal1, diagonal2))

