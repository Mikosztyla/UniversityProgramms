# Zadanie 13. Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami
# pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy, dla
# którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t=
# [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.

import random

n = int(input("Podaj zakres: "))
tab = [random.randint(1, 10) for _ in range(n)]
# tab = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
# n = len(tab)
print(tab)
max_length = length = 0
for i in range(n):
    for j in range(n-1, -1, -1):
        length = 0
        while tab[i] == tab[j] and i < j:
            length += 1
            i += 1
            j -= 1
        max_length = max(max_length, length)

print(max_length)