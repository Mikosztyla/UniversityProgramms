# Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
# True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
# False w przeciwnym przypadku.
import random


def check_zero(tab, n):
    rows = [False for _ in range(n)]
    cols = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in rows:
        if not i:
            return False
    for i in cols:
        if not i:
            return False
    return True


n = int(input("Podaj zakres: "))
tab = [[random.randint(-1, 1) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

print(check_zero(tab, n))