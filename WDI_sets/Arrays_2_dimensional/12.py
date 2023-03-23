# Zadanie 12. Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy
# tablicę wypełnioną liczbami większymi od zera. Funkcja powinna zwracać wartość True, jeżeli
# na wszystkich poziomach tablicy liczba elementów sąsiadujących (w obrębia poziomu) z co najmniej
# 6 liczbami złożonymi jest jednakowa albo wartość False w przeciwnym przypadku.
import random
import math


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    a = 5
    while a < math.sqrt(x) + 1:
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def check_level(tab):
    result = 0
    moves = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            s = 0
            for move in moves:
                a, b = move
                if not is_prime(tab[i + a][j + b]):
                    s += 1
            if s >= 6:
                result += 1
    return result


def check_tab(tab):
    first = check_level(tab[0])
    for i in range(1, n):
        number = check_level(tab[i])
        if number != first:
            return False
    return True


n = int(input("Podaj rozmiar trojwymiarowej tablicy: "))
tab = [[[random.randint(1, 20) for _ in range(n)] for _ in range(n)] for _ in range(n)]
#tab = [[[5, 10, 12], [7, 16, 20], [18, 16, 10]], [[14, 19, 20], [14, 5, 7], [9, 4, 15]], [[4, 14, 2], [20, 3, 12], [1, 14, 4]]]
print(tab)
print(check_tab(tab))