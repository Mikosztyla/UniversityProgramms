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