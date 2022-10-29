n = int(input("Podaj liczbę: "))
a = 2
b = 5
while n%a != 0 and a < n:
    a += b
    b *= 3
if n%a == 0:
    print(True)
else:
    print(False)