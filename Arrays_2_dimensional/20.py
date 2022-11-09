# Zadanie 20. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
import random


def get_sums(tab, rows, cols):
    for i in range(n):
        for j in range(n):
            rows[i] += tab[i][j]
            cols[j] += tab[i][j]


def get_position_of_towers(tab):
    rows = [0 for _ in range(n)]
    cols = [0 for _ in range(n)]
    max_sum = 0
    w = 0
    get_sums(tab, rows, cols)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if i != k or j != l:
                        s = 0
                        if i == k:
                            s = rows[i] + cols[j] + cols[l] - 2 * tab[i][j] - 2 * tab[k][l]
                        elif j == l:
                            s = cols[j] + rows[i] + rows[l] - 2 * tab[i][j] - 2 * tab[k][l]
                        else:
                            s = rows[i] + cols[j] - 2 * tab[i][j] + rows[k] + cols[l] - 2 * tab[k][l] - tab[i][l] - tab[k][j]

                        if s > max_sum:
                            max_sum = s
                            w = ((i, j), (k, l))
    return w, max_sum


n = int(input("Podaj rozmiar tablicy: "))
tab = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]
# tab = [
# [0, 1, 1, 0],
# [0, 1, 1, 0],
# [0, 1, 1, 1],
# [0, 1, 1, 0]
# ]
for i in range(n):
    print(tab[i])
print()

print(get_position_of_towers(tab))