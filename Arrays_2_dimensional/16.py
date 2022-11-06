# Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Prosze napisac funkcje która
# odpowiada na pytanie, czy w tablicy kazdy wiersz zawiera co najmniej jedna liczba złozona wyłacznie z cyfr
# bedacych liczbami pierwszymi?
import random


def is_prime(x):
    while x > 0:
        if x % 10 != 2 and x % 10 != 3 and x % 10 != 5 and x % 10 != 7:
            return False
        x //= 10
    return True


def check_rows(tab, n):
    for i in range(n):
        check_row = False
        for j in range(n):
            if not check_row and is_prime(tab[i][j]):
                check_row = True
        if not check_row:
            return False
    return True


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
# tab = [
# [28, 4, 77, 30, 26],
# [27, 28, 1, 20, 29],
# [19, 5, 35, 27, 14],
# [26, 29, 72, 4, 9],
# [9, 52, 16, 19, 18]
# ]
for i in range(n):
    print(tab[i])

print(check_rows(tab, n))