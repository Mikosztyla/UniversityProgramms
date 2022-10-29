def ile25(x):
    count2 = 0
    count5 = 0
    while x % 2 == 0:
        x //= 2
        count2 += 1

    while x % 5 == 0:
        x //= 5
        count5 += 1

    if count2 > count5:
        return count2
    else:
        return count5


def skr(l, m):
    a, b = l, m
    while b > 0:
        a, b = b, a % b
    return l//a, m//a


def ula(l, m):
    l, m = skr(l, m)
    print(l//m, end="")
    l %= m
    if l != 0:
        print(",", end="")
        for _ in range(ile25(m)):
            l *= 10
            print(l//m, end="")
            l %= m
        if l != 0:
            print("(", end="")
            mem = l
            while True:
                l *= 10
                print(l // m, end="")
                l %= m
                if l == mem:
                    break
            print(")", end="")


ula(1, 14)