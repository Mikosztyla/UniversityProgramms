# Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta zawiera cyfrę równą liczbie swoich cyfr

n = int(input("Podaj liczbę: "))
is_digit = False
x = n
s = 0
while x > 0:
    s += 1
    x //= 10

while n > 0 and not is_digit:
    x = n % 10
    if x == s:
        is_digit = True
    n //= 10

print(is_digit)