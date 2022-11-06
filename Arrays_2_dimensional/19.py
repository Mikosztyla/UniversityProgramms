# Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.
import random


def get_pairs(tab, moves, n, k):
    already_checked = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if not already_checked[i][j]:
                already_checked[i][j] = True
                for move in moves:
                    x, y = move
                    if 0 <= i + x < n and 0 <= j + y < n:
                        if tab[i][j] * tab[i+x][j+y] == k:
                            result += 1
                            print(tab[i][j], tab[i+x][j+y])
                            already_checked[i+x][j+y] = True
    return result


n = int(input("Podaj zakres: "))
k = int(input("Podaj iloczyn: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
print(get_pairs(tab, moves, n, k))