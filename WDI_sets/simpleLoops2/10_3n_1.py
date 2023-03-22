# Zadanie 10. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
# jest równy 2.

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