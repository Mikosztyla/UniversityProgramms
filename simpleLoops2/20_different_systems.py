def change_system(x, s):
    t = [0 for i in range(64)]
    iterator = 0
    while x > 0:
        t[iterator] = x % s
        x //= s
        iterator += 1

    for i in range(iterator-1, -1, -1):
        print("0123456789ABCDEF"[t[i]], end="")


def is_different(a, b):
    digits = [0 for i in range(10)]
    while a > 0:
        digits[a % 10] += 1
        a //= 10
    while b > 0:
        if digits[b % 10] != 0:
            return False
        b //= 10
    return True

print(is_different(123, 345))