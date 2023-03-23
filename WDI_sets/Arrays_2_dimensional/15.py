# Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
# będącą liczbą pierwszą?
import random
import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
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


def row_with_prime_numbers(tab, n):
    for i in range(n):
        all_numbers_prime = True
        for j in range(n):
            if all_numbers_prime:
                if not is_prime(tab[i][j]):
                    all_numbers_prime = False
        if all_numbers_prime:
            return True
    return False


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

print(row_with_prime_numbers(tab, n))