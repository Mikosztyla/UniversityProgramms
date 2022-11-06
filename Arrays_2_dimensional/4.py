# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.
import random


def get_sums(rows, cols, tab, n):
    for i in range(n):
        for j in range(n):
            rows[i] += tab[i][j]
            cols[j] += tab[i][j]


def get_max(tab, n):
    result = tab[0]
    index = 0
    for i in range(1, n):
        if tab[i] > result:
            result = tab[i]
            index = i
    return index


def get_min(tab, n):
    result = tab[0]
    index = 0
    for i in range(1, n):
        if tab[i] < result:
            result = tab[i]
            index = i
    return index


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

rows = [0 for _ in range(n)]
cols = [0 for _ in range(n)]

get_sums(rows, cols, tab, n)

# print()
# print()
# print(cols)
# print(rows)
max_col_sum = get_max(cols, n)
min_row_sum = get_min(rows, n)

print(f"kolumna: {max_col_sum} wiersz: {min_row_sum}")