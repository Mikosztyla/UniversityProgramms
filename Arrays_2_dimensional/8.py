# Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu.
import random


def get_diagonals(tab, n):
    max_length = 0
    for j in range(n-3, -1, -1):
        temp = [0 for _ in range(n)]
        i = 0
        iterator = 0
        while i < n and j < n:
            temp[iterator] = tab[i][j]
            iterator += 1
            i += 1
            j += 1
        print(temp)
        max_length = max(check_geometrical(temp, iterator), max_length)

    for i in range(1, n-2):
        j = 0
        temp = [0 for _ in range(n)]
        iterator = 0
        while i < n and j < n:
            temp[iterator] = tab[i][j]
            iterator += 1
            i += 1
            j += 1
        print(temp)
        max_length = max(check_geometrical(temp, iterator), max_length)

    if max_length >= 3:
        return max_length
    else:
        return "Nie udało się znaleźc ciągu geometrycznego, który ma conajmniej 3 elementy"


def check_geometrical(tab, n):
    q = 1
    max_length = 0
    length = 1
    for i in range(1, n):
        if tab[i] / tab[i - 1] == q:
            length += 1
        else:
            q = tab[i] / tab[i - 1]
            length = 2
        max_length = max(max_length, length)
    return max_length


n = int(input("Podaj zakres (co najmniej 3): "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
# tab = [
# [3, 8, 2, 5, 1, 4],
# [10, 10, 2, 2, 5, 10],
# [1, 2, 9, 1, 5, 5],
# [8, 6, 4, 10, 10, 7],
# [4, 1, 3, 8, 4, 7],
# [2, 2, 6, 5, 16, 8]]
# n = len(tab)
for i in range(n):
    print(tab[i])
print()

print(get_diagonals(tab, n))