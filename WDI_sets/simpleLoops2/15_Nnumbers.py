# Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
# liczby jest równa tej liczbie, np. 153 = 13 + 53 + 33

digits = 1
number = 9
for i in range(1000000):
    if i > number:
        digits += 1
        number = number * 10 + 9
    s = 0
    x = i
    while x > 0:
        s += pow(x % 10, digits)
        x //= 10
    if s == i:
        print(i)