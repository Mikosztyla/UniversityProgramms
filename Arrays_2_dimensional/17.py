# Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.
import random


def best_neighbours(tab, n):
    max_s, s = 0, 0
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(n):
            s = 0
            if i - 1 >= 0:
                s += tab[i-1][j]
            if j + 1 < n:
                s += tab[i][j+1]
            if i + 1 < n:
                s += tab[i+1][j]
            if j - 1 >= 0:
                s += tab[i][j-1]

            if s > max_s:
                max_s = s
                max_i = i
                max_j = j
    return max_i, max_j, max_s


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

print(best_neighbours(tab, n))