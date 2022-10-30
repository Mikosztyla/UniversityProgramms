import random

# n = int(input("Podaj ile ma byc elementow w tablicy: "))
# tab = [random.randint(1, 100) for i in range(n)]
tab = [6, 4, 6, 8, 10, 3, -4, -11, -18, 20, 5, 30, 35]
print(tab)
length = 1
maxLength = 1
r = tab[1] - tab[0]
for i in range(1, len(tab)):
    if tab[i] - tab[i-1] == r:
        length += 1
    else:
        if length >= maxLength:
            maxLength = length
        length = 2
        r = tab[i] - tab[i-1]
print(max(maxLength, length))