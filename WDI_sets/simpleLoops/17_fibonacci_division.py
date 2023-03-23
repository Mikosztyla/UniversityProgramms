# Zadanie 17. Prosze napisac program wyznaczajacy wartosc do której zmierza iloraz dwóch kolejnych
# wyrazów ciagu Fibonacciego. Wyznaczyc ten iloraz dla róznych wartosci poczatkowych wyrazów ciagu.

eps = 1/1000000
a, b = 1, 1
d = a/b
previous_d = 0
while abs(previous_d-d) > eps:
    previous_d = d
    a, b = b, a + b
    d = a/b
print(d)
# zawsze ciąg zmierza do wartości 0.618033