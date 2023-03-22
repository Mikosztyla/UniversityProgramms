# Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
# np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
# która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
# elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
# pozostać nie zmieniane.
import random


def print_tab(tab):
    for i in range(len(tab)):
        print(tab[i])
    print()


def count_ones(x):
    s = 0
    while x > 0:
        if x % 2 == 1:
            s += 1
        x //= 2
    return s


def get_cords(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    sums1 = [[0 for _ in range(n1)] for _ in range(n1)]
    sums2 = [[0 for _ in range(n2)] for _ in range(n2)]
    for i in range(n1):
        for j in range(n1):
            sums1[i][j] = count_ones(tab1[i][j])
    for i in range(n2):
        for j in range(n2):
            sums2[i][j] = count_ones(tab2[i][j])
    #print_tab(sums1)
    #print_tab(sums2)

    for i in range(n2 - n1 + 1):
        for j in range(n2 - n1 + 1):
            s = 0
            for k in range(n1):
                for l in range(n1):
                    if sums1[k][l] == sums2[i + k][j + l]:
                        s += 1
            min_s = (n1 ** 2) // 3
            if s > min_s:
                return True, i, j
    return False


n1 = int(input("Podaj zakres pierwszej tablicy: "))
n2 = int(input("Podaj zakres drugie tablicy (musi być wieksze niz pierwszy): "))

tab1 = [[random.randint(1, 20) for _ in range(n1)] for _ in range(n1)]
tab2 = [[random.randint(1, 20) for _ in range(n2)] for _ in range(n2)]
# tab1 = [
#     [20, 6],
#     [2, 3]
# ]
#
# tab2 = [
#     [19, 19, 15],
#     [1, 19, 17],
#     [10, 10, 3]
# ]
print_tab(tab1)
print_tab(tab2)

print(get_cords(tab1, tab2))