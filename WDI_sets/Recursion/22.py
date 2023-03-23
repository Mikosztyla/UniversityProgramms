# Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
import random


def sprawdz_tab(T, p=0):
    if p == len(T)-1:
        print(p)
        return True
    if p >= len(T):
        return False
    liczba = T[p]
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            while liczba % dzielnik == 0:
                liczba //= dzielnik
            if dzielnik < T[p]:
                if sprawdz_tab(T, p+dzielnik):
                    print(p)
                    return True
        dzielnik += 1
    return False


T = [random.randint(1, 100) for _ in range(10)]
print(T)
print(sprawdz_tab(T))
