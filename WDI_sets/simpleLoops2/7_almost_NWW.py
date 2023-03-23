# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

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