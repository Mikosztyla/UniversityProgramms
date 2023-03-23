# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.
n = int(input("Podaj zakres: "))

tab = [[0 for i in range(n)] for j in range(n)]
it_row = it_col = 0
counter = 0
for i in range(n):
    counter += 1
    tab[0][i] = counter
counter += 1
last = 1
while counter < n**2:
    for i in range(last, n-last):
        tab[i][n-last] = counter
        counter += 1
    for i in range(n-last, last-2, -1):
        tab[n-last][i] = counter
        counter += 1
    last += 1
    for i in range(n-last, last-2, -1):
        tab[i][last-2] = counter
        counter += 1
    for i in range(last-1, n-last + 1):
        tab[last-1][i] = counter
        counter += 1
for i in range(n):
    print(tab[i])