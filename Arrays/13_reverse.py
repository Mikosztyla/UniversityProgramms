import random

n = int(input("Podaj zakres: "))
tab = [random.randint(1, 10) for _ in range(n)]
#tab = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
#n = len(tab)
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