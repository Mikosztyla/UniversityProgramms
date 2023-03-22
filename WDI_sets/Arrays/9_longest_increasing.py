# Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu rosnącego.

import random

n = int(input("Podaj ile ma byc elementow w tablicy: "))
tab = [random.randint(1, 100) for i in range(n)]
# tab = [40, 51, 74, 14, 55, 48, 16, 36, 76, 41]
print(tab)
length = 1
maxLength = 1
for i in range(1, n):
    if tab[i] > tab[i-1]:
        length += 1
    else:
        if length >= maxLength:
            maxLength = length
        length = 1
print(max(maxLength, length))