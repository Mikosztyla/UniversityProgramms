n = int(input("Podaj liczbę: "))
a = 3
b = 4
while n%a != 0 and a < n:
    a += b
    b += 2
if n%a == 0:
    print(True)
else:
    print(False)