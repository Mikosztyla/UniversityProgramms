# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe pocięcie
# liczby N na kawałki, tak aby każdy z kawałków był liczbą pierwszą oraz liczba kawałków też była liczba pierwszą.
# Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na 23 i 47,
# natomiast divide(2255)=False
import math


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    a = 5
    while a < x**0.5 + 1:
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def divide(number, curr_number=0, it=0, n=0):
    if it == int(math.log10(number)) + 1:
        if is_prime(n) and curr_number == 0:
            print(n)
            return True
        else:
            return False

    curr_number = curr_number * 10 + (number % 10**(int(math.log10(number)) + 1 - it))//(10**(int(math.log10(number)) - it))
    if is_prime(curr_number):
        if divide(number, 0, it+1, n+1):
            return True
    if divide(number, curr_number, it+1, n):
        return True
    return False


print(divide(23672))
