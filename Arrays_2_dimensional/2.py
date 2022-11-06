# Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.
import random


def has_odd_digit(number):
    while number > 0:
        if number % 2 == 0:
            return False
        number //= 10
    return True


def odd_in_every_row(tab, n):
    for i in range(n):
        for j in range(n):
            if has_odd_digit(tab[i][j]):
                s = True
                break
        else:
            return False
    return True

n = int(input("Podaj zakres: "))

tab = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

for i in range(n):
    print(tab[i])

print(odd_in_every_row(tab, n))