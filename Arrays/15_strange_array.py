import math


def is_prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True


def check_tab(tab, n):
    a, b = 1, 2
    s = 0
    for i in range(n):
        if i == a:
            if is_prime(tab[a]):
                return False
            a, b = b, a + b
        else:
            if is_prime(tab[i]):
                s = 1
    if s == 1:
        return True
    return False

tab = [3, 10, 124, 6, 4, 12, 345, 6, 80]

n = len(tab)
print(check_tab(tab, n))
