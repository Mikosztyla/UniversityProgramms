# Zadanie 18. Mamy dane dwa ciągi A,B o następujących zależnościach:
# A: a0 = 0, a1 = 1, an = an−1 − bn−1 ∗ an−2
# B: b0 = 2, bn = bn−1 + 2 ∗ an−1
# Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
# kolejnymi wyrazami ciągu An (tj. a0, a1, a2, ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn
# (tj. b0, b1, b2, ...).

# 0 1 1 5
# 2 2 4 6

a1 = 0
a2 = 1
b1 = 2
b2 = 2
for i in range(0, 10):
    a_temp = a2 - b2 * a1
    b_temp = b2 + 2 * a2
    print(a_temp, b_temp)
    a1, a2 = a2, a_temp
    b1, b2 = b2, b_temp