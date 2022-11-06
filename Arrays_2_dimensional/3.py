# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.
import random


def has_even_digit(number):
    while number > 0:
        if number % 2 == 0:
            return True
        number //= 10
    return False


def odd_in_every_row(tab, n):
    for i in range(n):
        for j in range(n):
            if not has_even_digit(tab[i][j]):
                break
        else:
            return True
    return False

n = int(input("Podaj zakres: "))

tab = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

for i in range(n):
    print(tab[i])

print(odd_in_every_row(tab, n))