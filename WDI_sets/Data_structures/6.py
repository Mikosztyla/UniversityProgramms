# Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
# im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
# odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.

#from math import sin, cos, arctan

class Zespolone():
    def __init__(self, re, im):
        self.liczba = (re, im)
        self.module = (re**2 + im**2)**.5

    def wypisz(self):
        result = str(self.liczba[0]) + ' + ' + str(self.liczba[1]) + 'i'
        print(result)

    def __add__(self, other):
        result = Zespolone(self.liczba[0] + other.liczba[0], self.liczba[1] + other.liczba[1])
        return result


z = Zespolone(3, 4) + Zespolone(2, 1)
z.wypisz()
