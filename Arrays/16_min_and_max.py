import random


def is_uniq(tab):
    minim = maxim = tab[0]
    min_count = max_count = 1
    for i in range(1, len(tab)):
        if tab[i] >= maxim:
            if tab[i] == maxim:
                max_count += 1
            else:
                maxim = tab[i]
                max_count = 1
        elif tab[i] <= minim:
            if tab[i] == minim:
                min_count += 1
            else:
                minim = tab[i]
                min_count = 1
    if max_count > 1 or min_count > 1:
        return False
    return True

tab = [random.randint(1, 100) for _ in range(20)]
#tab = [32, 6, 4, 8, 1, 234, 5, 346, 7, 3, 1, 346]
print(tab)

print(is_uniq(tab))

