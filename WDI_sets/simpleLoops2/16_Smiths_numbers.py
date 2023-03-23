# Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący
# liczby Smitha mniejsze od 1000000.

import math


def get_dividors(n):
    s = 0
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            s += get_sum_of_number(i)
            n //= i
    if n > 1:
        s += get_sum_of_number(n)
    return s


def get_sum_of_number(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

#n = int(input("Podaj liczbę, a ja ci powiem czy ona należy do Smitha: "))
# list = [4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346,
#         355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576,
#         588, 627, 634, 636, 645, 648, 654, 663, 666, 690, 706, 728,
#         729, 762, 778, 825, 852, 861, 895, 913, 915, 922, 958, 985,1086]
#list = [27]
s = 0
for i in range(1000000):
    if get_sum_of_number(i) == get_dividors(i):
        print(i)
        s += 1
print(s)