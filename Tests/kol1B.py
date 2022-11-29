import math


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    a = 5
    while a < math.sqrt(x)+1:
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def get_max_number(tab):
    l = len(tab)
    curr_mult = 1
    max_number_it = 0
    for i in range(l):
        if curr_mult != 1 and tab[i] == curr_mult:
            max_number_it = i
        if is_prime(tab[i]):
            curr_mult *= tab[i]

    if max_number_it == 0:
        return False
    else:
        return max_number_it


tab = [1, 1, 2, 1, 0, 2, 2]
print(get_max_number(tab))
