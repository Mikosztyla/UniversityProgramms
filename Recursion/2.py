# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    a = 5
    while a < (x**.5 + 1):
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def waga(x):
    wynik = 0
    dzielnik = 2
    while x > 1:
        if is_prime(dzielnik) and x % dzielnik == 0:
            wynik += 1
        while x % dzielnik == 0:
            x //= dzielnik
        dzielnik += 1
    return wynik


def sprawdz_wagi(T):
    l = len(T)
    tab = [-1 for _ in range(3)]
    ilosc_podzbiorów = 0
    for el in T:
        temp = waga(el)
        juz_w_podzbiorze = False
        for i in range(ilosc_podzbiorów):
            if tab[i] == temp:
                juz_w_podzbiorze = True
        if not juz_w_podzbiorze:
            if ilosc_podzbiorów < 3:
                tab[ilosc_podzbiorów] = temp
                ilosc_podzbiorów += 1
            else:
                return False
    return True


print(sprawdz_wagi([5, 2, 6, 4, 70, 1]))