# Zadanie 5. Prosze napisac program wyznaczajacy pierwiastek kwadratowy ze wzoru Newtona.

eps = 1/1000000
n = 50
y, x = 1, 0
while abs(x-y) > eps:
    x = y
    y = (n/x + x)/2
print(x)