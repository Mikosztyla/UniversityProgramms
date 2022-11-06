# Zadanie 11. Dwie liczby naturalne sa „przyjaciółkami jezeli zbiory cyfr z których zbudowane sa liczby
# sa identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Prosze napisac funkcje, która dla tablicy T zwraca ile elementów tablicy sasiaduje wyłacznie z
# przyjaciółkami
import random


def check_digits(a, b):
    tab1 = [False for _ in range(10)]
    tab2 = [False for _ in range(10)]
    while a > 0:
        tab1[a % 10] = True
        a //= 10
    while b > 0:
        tab2[b % 10] = True
        b //= 10

    for i in range(10):
        if tab1[i] != tab2[i]:
            return False
    return True


def check_tab(tab, n):
    result = 0
    for i in range(n):
        for j in range(n):
            s = 0
            s_max = 4
            if i - 1 >= 0:
                if check_digits(tab[i][j], tab[i-1][j]):
                    s += 1
            else:
                s_max -= 1
            if j + 1 < n:
                if check_digits(tab[i][j], tab[i][j+1]):
                    s += 1
            else:
                s_max -= 1
            if i + 1 < n:
                if check_digits(tab[i][j], tab[i+1][j]):
                    s += 1
            else:
                s_max -= 1
            if j - 1 >= 0:
                if check_digits(tab[i][j], tab[i][j-1]):
                    s += 1
            else:
                s_max -= 1

            if s == s_max:
                result += 1
    return result


n = int(input("Podaj zakres: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
# tab = [
# [8, 81, 12, 4, 1],
# [8, 11121, 1212, 21, 8],
# [6, 8, 2221, 7, 9],
# [34, 3, 1, 5, 1],
# [43, 443, 5, 55, 555]
# ]
for i in range(n):
    print(tab[i])

print(check_tab(tab, n))