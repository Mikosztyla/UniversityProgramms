# Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów
# wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
# że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do
# tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
import random


def get_dzielniki(l):
    dzielnik = 2
    global dzielniki
    while l > 1:
        if l % dzielnik == 0:
            dzielniki.append(dzielnik)
            while l % dzielnik == 0:
                l //= dzielnik
        dzielnik += 1


def iloczyny(T, p=0, res=[]):
    if len(res) > 0:
        print(res, end="")
        w = 1
        for el in res:
            w *= el
        print(" ->", w)
    if p == len(T):
        return
    for i in range(p, len(T)):
        iloczyny(T, i+1, res+[T[i]])
    return


liczba = random.randint(2, 1000)
print(liczba)
dzielniki = []
get_dzielniki(liczba)
print(dzielniki)
print()
iloczyny(dzielniki)