# Zadanie 8. Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego,
# np. 9,14,15,17,22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
# następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.

def is_in_Fib(x):
    a, b = 1, 1
    p, q = 1, 1
    s = 0
    while s < x:
        s += a
        a, b = b, a + b

    while s > x:
        s -= p
        p, q = q, p + q

    return s == x

n = int(input("Podaj liczbę, od której zacznie się program: "))
a = n + 1
while is_in_Fib(a):
    a += 1
print(a)