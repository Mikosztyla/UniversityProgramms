# Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Prosze napisac funkcje, która
# wyszuka spójny podciag elementów lezacy poziomo lub pionowo o najwiekszej sumie. Maksymalna długosc
# podciagu moze wynosic 10 elementów. Do funkcji nalezy przekazac tablice T, funkcja powinna zwrócic sume
# maksymalnego podciagu.
import random


def max_sum(tab, n):
    max_s = 0
    length = 0
    curr_s = 0
    for i in range(n):
        if length < 10:
            if curr_s + tab[i] > 0:
                curr_s += tab[i]
                length += 1
            else:
                curr_s = 0
                length = 0
        else:
            curr_s += tab[i]
            curr_s -= tab[i-10]

        if curr_s > max_s:
            max_s = curr_s
    return max_s


def check_tab(tab, n):
    max_s = 0
    for i in range(n):
        s = max_sum(tab[i], n)
        if max_s < s:
            max_s = s
    for i in range(n):
        s = max_sum([tab[j][i] for j in range(n)], n)
        if max_s < s:
            max_s = s
    return max_s


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

print(check_tab(tab, n))