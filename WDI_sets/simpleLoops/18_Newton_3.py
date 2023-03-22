# Zadanie 18. Prosze zmodyfikowac wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.

eps = 1/1000000
n = 50
y, x = 1, 0
while abs(x-y) > eps:
    x = y
    y = (n/(x*x) + 2*x)/3
print(x)