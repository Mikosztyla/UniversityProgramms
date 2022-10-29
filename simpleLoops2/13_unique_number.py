n = int(input("Podaj liczbę: "))
a = n%10
n //= 10
is_unique = True
while n > 0 and is_unique:
    x = n % 10
    if x == a:
        is_unique = False
    n //= 10
print(is_unique)
