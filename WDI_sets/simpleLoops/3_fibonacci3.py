# Zadanie 3. Prosze napisac program sprawdzajacy czy istnieje spójny podciag ciagu Fibonacciego o zadanej
# sumie.

a, b, c, d = 1, 1, 1, 1
dana_suma = 33
suma = 0

while suma < dana_suma:
    suma += a
    a, b, = b, a+b

while suma > dana_suma:
    suma -= c
    c, d = d, c+d

if suma == dana_suma:
    print(True)
    while suma > 0:
        print(c)
        suma -= c
        c, d = d, c+d
else:
    print(False)