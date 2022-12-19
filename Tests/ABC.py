import math


def increase_evens(x):
    number = 0
    l = int(math.log10(x))
    for i in range(l, -1, -1):
        number = number * 10 + x // (10 ** i)
        x %= 10 ** i
        if number % 2 == 0:
            number += 1
    return number


def ABC(x, y, k, n, last=0, res=[]): # 1 -> A, 2 -> B, 3 -> C
    result = 0
    if x == y:
        print(res)
        return 1
    if k == n:
        return 0

    for i in range(1, 4):
        if last != i:
            mem = x
            if i == 1:
                x += 3
            elif i == 2:
                x *= 2
            else:
                x = increase_evens(x)
            result += ABC(x, y, k + 1, n, i, res + [i])
            x = mem
    return result


#result = 0
print(ABC(11, 31, 0, 4))
