# Zadanie 24. Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.
import random
import math


def srodki_ciezkosci(tab, p = 0, suma_x = 0, suma_y = 0, ile = 0):
    if p == len(tab):
        result.append((suma_x/ile, suma_y/ile))
        return
    for i in range(p, len(tab)):
        srodki_ciezkosci(tab, i+1, suma_x + tab[i][0], suma_y + tab[i][1], ile + 1)
    return


def get_min_distance():
    min_dist = -1
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            result2.append(math.sqrt(abs(result[i][0] - result[j][0])**2 + abs(result[i][1] - result[j][1])**2))
            dist = result2[-1]
            if min_dist == -1:
                min_dist = dist
            else:
                min_dist = min(dist, min_dist)
    return min_dist


tab = [(random.randint(1, 9), random.randint(1, 9)) for _ in range(5)]
print(tab)
result = []
result2 = []
srodki_ciezkosci(tab)
#print(result)
print(get_min_distance())
result2.sort()
#print(result2)