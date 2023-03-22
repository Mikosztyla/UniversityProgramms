# Zadanie 7. Prosze napisac program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie,
# czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciagu Fibonacciego.

n = int(input())
a, b = 1, 1
while a*b < n:
    a, b = b, a+b
if a*b == n:
    print(True, a, b)
else:
    print(False)