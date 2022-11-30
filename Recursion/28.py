# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5, 7, 15] → f alse, podział nie istnieje.
import random


def count_ones(x):
    licznik = 1
    while x > 1:
        if x % 2 == 1:
            licznik += 1
        x //= 2
    return licznik


def binary(tab):
    global result
    result = [0 for _ in range(len(tab))]
    for i in range(len(tab)):
        result[i] = count_ones(tab[i])
    return result


def check_tab(T, p=0, s1=0, s2=0, s3=0):
    if p == len(T):
        return s1 == s2 == s3
    if check_tab(T, p+1, s1 + T[p], s2, s3):
        print("grupa 1:", tab[p])
        return True
    if check_tab(T, p+1, s1, s2 + T[p], s3):
        print("grupa 2:", tab[p])
        return True
    if check_tab(T, p+1, s1, s2, s3 + T[p]):
        print("grupa 3:", tab[p])
        return True
    return False


#tab = [random.randint(1, 10) for _ in range(10)]
tab = [2, 3, 5, 7, 15]
print(tab)
result = []
binary(tab)
print(result)
print(check_tab(result))
