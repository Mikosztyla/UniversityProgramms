# Zadanie 12. Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o
# ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
# indeksach.

import random

n = int(input("n: "))
tab = [0 for _ in range(n)]
for i in range(n):
    x = random.randint(1, 99)
    while x % 2 == 0:
        x = random.randint(1, 99)
    tab[i] = x

# tab = [13, 25, 2, 4, 6, 8, 10, 8, 6, 4]
print(tab)
inc_length = max_inc_length = 1
dec_length = max_dec_length = 1
r = tab[1] - tab[0]
inc_r = dec_r = 0
if r > 0:
    inc_r = r
elif r < 0:
    dec_r = r

for i in range(1, 10):
    r = tab[i] - tab[i-1]
    if r == inc_r:
        inc_length += 1
    elif r == dec_r:
        dec_length += 1
    else:
        if dec_length > max_dec_length:
            max_dec_length = dec_length
        dec_length = 2
        dec_r = 0

        if inc_length > max_inc_length:
            max_inc_length = inc_length
        inc_length = 2
        inc_r = 0

        if r > 0:
            inc_r = r
        else:
            dec_r = r

max_inc_length = max(max_inc_length, inc_length)
max_dec_length = max(max_dec_length, dec_length)
print(max_inc_length - max_dec_length)