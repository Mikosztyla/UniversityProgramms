# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.
import random
import math


def get_last_digit(n):
    return n%10


def get_first_digit(n):
    l = int(math.log10(n)) + 1
    return int(n/(10**(l-1)))


def get_distance(x, y):
    a = abs(7-x)
    b = abs(7-y)
    if b > a:
        a, b = b, a
    return b + (a-b)


def sprawdz(tab, x, y, path=[]):
    global moves
    if x == 7 and y == 7:
        return True
    for el in path:
        a, b = el
        if a == x and b == y:
            return False
    for move in moves:
        a, b = move
        if 0 <= x+a <= 7 and 0 <= y+b <= 7:
            if get_distance(x, y) >= get_distance(x+a, y+a):
                if get_last_digit(tab[x][y]) < get_first_digit(tab[x+a][y+b]):
                    if sprawdz(tab, x+a, y+b, path + [(x, y)]):
                        print(x+a, y+b)
                        return True
    return False


# tab = [[random.randint(10, 99) for _ in range(8)] for _ in range(8)]
# for i in range(8):
#     print(tab[i])
tab = [
[63, 53, 57, 38, 57, 49, 84, 49],
[88, 40, 97, 30, 76, 69, 45, 17],
[26, 61, 23, 21, 18, 36, 30, 21],
[67, 88, 29, 40, 41, 50, 69, 13],
[86, 89, 96, 95, 45, 59, 55, 55],
[49, 94, 39, 66, 49, 75, 15, 42],
[81, 40, 60, 97, 51, 23, 93, 43],
[76, 58, 11, 24, 77, 20, 36, 86]
]
moves = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
print(sprawdz(tab, 0, 0))
