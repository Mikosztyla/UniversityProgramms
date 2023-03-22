# Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.

import random


def has_only_odd_numbers(x):
    while x > 0:
        if x % 2 == 0:
            return False
        x //= 10
    return True

n = int(input("Podaj ile ma byc elementow w tablicy: "))
tab = [random.randint(1, 1000) for i in range(n)]
#print(tab)
for x in tab:
    if has_only_odd_numbers(x):
        print("Istnieje taki element, ktory ma same cyfry nieparzyste: ", x)
        break
else:
    print("Wszystkie liczby w tablicy mają co najmniej jedna liczbe parzysta")