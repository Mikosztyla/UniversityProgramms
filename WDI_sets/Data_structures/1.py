# Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
# licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.


def mnozenie(a, b, c, d):
    return a * c, b * d


def dzielenie(a, b, c, d):
    return a * d, b * c


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(a, b):
    return (a*b)//nwd(a, b)


def dodawanie(a, b, c, d):
    return a * nww(b, d)//b + c * nww(b, d)//d, nww(b, d)


def odejmowanie(a, b, c, d):
    return a * nww(b, d) // b - c * nww(b, d) // d, nww(b, d)


def skroc(a, b):
    return a//nwd(a, b), b//nwd(a, b)


print(dzielenie(2, 5, 1, 10))