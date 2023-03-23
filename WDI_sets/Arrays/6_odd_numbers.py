# Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy każdy
# element tablicy zawiera co najmniej jedną cyfrę nieparzystą.

import random

def has_odd_number(x):
    while x > 0:
        if x % 2 == 1:
            return True
        x //= 10
    return False

n = int(input("Podaj ile ma byc elementow: "))
tab = [random.randint(1, 1000) for i in range(n)]
#print(tab)
for x in tab:
    if not has_odd_number(x):
        print("Jest liczba, która ma same liczby parzyste: ", x)
        break
else:
    print("Wszystkie liczby maja conajmniej jedna cyfre nieparzysta")