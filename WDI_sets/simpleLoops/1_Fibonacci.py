# Zadanie 1. Prosze napisac program wypisujacy elementy ciagu Fibonacciego mniejsze od miliona.

a, b = 1, 1
while a < 1000000:
    print(a)
    a, b = b, a+b