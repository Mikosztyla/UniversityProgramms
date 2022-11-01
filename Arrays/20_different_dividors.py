def is_valid(n, product):
    if product % n == 0:
        return False
    divisor = 2
    already_divided = False
    while n > 1:
        if n % divisor == 0:
            if product % divisor == 0 or already_divided:
                return False
            already_divided = True
            n //= divisor
        else:
            divisor += 1
            already_divided = False
    return True


tab = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
dl = len(tab)

i, j = 0, 0
curr_length = max_length = 1
curr_product = tab[0]
while j < dl-1:
    if is_valid(tab[j + 1], curr_product):
        curr_product *= tab[j + 1]
        j += 1
        curr_length += 1
        max_length = max(max_length, curr_length)
    else:
        if curr_product == 1:
            i += 1
            j += 1
        else:
            curr_product //= tab[i]
            i += 1
            curr_length -= 1
print(max_length)