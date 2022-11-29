# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
import random
import math


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    a = 5
    while a < math.sqrt(x) + 1:
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def cut_number(n):
    l = int(math.log10(n)+1)
    if l > 1:
        mult = 1
        for i in range(l):
            number = n // (mult * 10) * mult + n % mult
            if is_prime(number):
                print("liczba pierwsza:", number)
            mult *= 10
            cut_number(number)


n = random.randint(1000, 10000)
print(n)
cut_number(n)
