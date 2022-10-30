import random

def has_odd_number(x):
    while x > 0:
        if x % 2 == 1:
            return True
        x //= 10
    return False

n = int(input("Podaj ile ma byc elementow: "))
tab = [random.randint(1, 1000) for i in range(n)]
#print(tab)
for x in tab:
    if not has_odd_number(x):
        print("Jest liczba, która ma same liczby parzyste: ", x)
        break
else:
    print("Wszystkie liczby maja conajmniej jedna cyfre nieparzysta")