# Zadanie 2. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def have_same_digits(a, b):
    digits = [0 for i in range(10)]
    while a > 0:
        digits[a % 10] += 1
        a //= 10
    while b > 0:
        digits[b % 10] -= 1
        b //= 10

    for i in digits:
        if i != 0:
            return False
    return True


a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
print(have_same_digits(a, b))