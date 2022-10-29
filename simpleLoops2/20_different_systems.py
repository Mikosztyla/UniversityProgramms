def is_different(a, b, s):
    digits = [0 for i in range(s)]
    while a > 0:
        digits[a % s] += 1
        a //= s
    while b > 0:
        if digits[b % s] != 0:
            return False
        b //= s
    return True

a = 123
b = 522

for i in range(2, 17):
    if is_different(a, b, i):
        print(i)
        break
else:
    print("Nie istnieje taka podstawa")