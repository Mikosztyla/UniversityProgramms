# Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość
# najdłuższego, spójnego podciągu geometrycznego.

import random

# n = int(input("Podaj ile ma byc elementow w tablicy: "))
# tab = [random.randint(1, 100) for i in range(n)]
tab = [-1, 4, 8, 16, 32, 16, 8, 4, 2, 1, 5, 30, 35]
print(tab)
length = 1
maxLength = 1
q = tab[1]/tab[0]
for i in range(1, len(tab)):
    if tab[i] / tab[i-1] == q:
        length += 1
    else:
        if length >= maxLength:
            maxLength = length
        length = 2
        q = tab[i] / tab[i-1]
print(max(maxLength, length))