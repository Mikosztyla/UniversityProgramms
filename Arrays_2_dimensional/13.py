# Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
# T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
# liczby komplementarnej.
import random
import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 0:
        return False
    x = 5
    while x < math.sqrt(n) + 1:
        if n % x == 0:
            return False
        x += 2
        if n % x == 0:
            return False
        x += 4
    return True


def check_tab(tab, n):
    for i in range(n):
        for j in range(n):
            has_pair = False
            for k in range(n):
                if not has_pair:
                    for l in range(n):
                        if (k != i or l != j) and tab[k][l] > 0:
                            s = tab[i][j] + tab[k][l]
                            if is_prime(tab[i][j] + tab[k][l]):
                                has_pair = True
            if not has_pair:
                tab[i][j] = 0
    for i in range(n):
        print(tab[i])


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

for i in range(n):
    print(tab[i])
print()

check_tab(tab, n)