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