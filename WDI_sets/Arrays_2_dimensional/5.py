# Zadanie 5. Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi
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

    curr_max = result
    index2 = 0
    for i in range(0, n):
        if curr_max > tab[i] > 0:
            curr_max = tab[i]
            index2 = i
    return index, index2


def get_min(tab, n):
    result = tab[0]
    index = 0
    for i in range(1, n):
        if tab[i] < result:
            result = tab[i]
            index = i

    curr_min = result
    index2 = 0
    for i in range(0, n):
        if curr_min < tab[i] < 0:
            curr_max = tab[i]
            index2 = i
    return index, index2


n = int(input("Podaj zakres: "))
tab = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
# tab = [
# [-6, -8, 8],
# [3, -8, 10],
# [-9, 8, 6],
# ]
for i in range(n):
    print(tab[i])

rows = [0 for _ in range(n)]
cols = [0 for _ in range(n)]

get_sums(rows, cols, tab, n)

# print()
# print(cols)
# print(rows)
# max_col_sum, max_col_sum2 = get_max(cols, n)
# min_row_sum, min_row_sum2 = get_min(rows, n)
print()
print(cols, rows)
result_col, result_row = 0, 0
# if cols[max_col_sum] > 0:
#     result_col = max_col_sum
#     x, y = get_max(rows, n)
#     if rows[y] > 0:
#         result_row = y
#     else:
#         result_row = min_row_sum2
# else:
#     x, y = get_min(cols, n)
#     if rows[min_row_sum] > 0:
#         result_col = max_col_sum
#         result_row = min_row_sum
#     else:
#         result_col = x
#         result_row = min_row_sum

cols2 = [0 for i in range(4)]
rows2 = [0 for i in range(4)]
a, b = get_max(cols, n)
cols2[0], cols2[1] = a, b
a, b = get_min(cols, n)
cols2[2], cols2[3] = a, b
a, b = get_max(rows, n)
rows2[0], rows2[1] = a, b
a, b = get_min(rows, n)
rows2[2], rows2[3] = a, b
result = 0
for i in range(4):
    for j in range(4):
        if cols[cols2[i]] / rows[rows2[j]] > result:
            result = cols[cols2[i]] / rows[rows2[j]]
            result_col = cols2[i]
            result_row = rows2[j]



print(f"kolumna: {result_col} wiersz: {result_row}")