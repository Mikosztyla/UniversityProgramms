# Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
# liczby jest równa tej liczbie, np. 153 = 13 + 53 + 33

import time


# tab = [i for i in range(1, 32)]
#
# for i in tab:
#     for j in range(5):
#         print(i%2, end="")
#         i = i >> 1
#     print()

# a = 115132219018763992565095597973971522401
# print(a-1)
def combinations(x):
    zbior = [-1 for i in range(x)]
    powers = [i for i in range(0, 11)]
    powers[10] = 0
    j = x-1
    s = 0
    digits = 1
    max_c = [9 for i in range(x)]
    suma = 0
    maxim = 10
    lower_max = 0
    zbior[x-1] = 0
    final = 0
    while True:
        # if zbior == max_c:
        #     for k in range(x-1, x-1-digits, -1):
        #         zbior[k] = 9
        # else:
        if suma > maxim:
            zbior[x-1] = 9
        else:
            s += 1
            # for i in range(x-1, x-1-digits, -1):
            #     print(zbior[i], end="")
            # print()
            #print("suma: ", suma)
            if suma >= lower_max:
                if check_if_armstrong(suma, zbior, digits, x):
                    print(suma)
                    final += 1

        if zbior[x-1] < 9:
            j = x - 1
            zbior[j] += 1
            suma += powers[zbior[j]] - powers[zbior[j]-1]
        else:
            j = x - 2
            while j >= 0 and zbior[j] == zbior[j+1]:
                j -= 1
            if j >= 0:
                if zbior[j] == -1:
                    digits += 1
                    print("--- %s seconds ---" % (time.time() - start_time), "  digits:  ", digits)
                    #max_c = max_combination(powers, digits, x)
                    lower_max = maxim - 1
                    maxim *= 10
                    for i in range(2, 10):
                        powers[i] *= i

                zbior[j] += 1
                suma = 0
                for l in range(x-digits, j+1):
                     suma += powers[zbior[l]]

                for k in range(j, x-1):
                    zbior[k+1] = zbior[k]
                    suma += powers[zbior[k+1]]
        if j < 0:
            break
    print("Liczba kombinacji: ", s, " liczby Armstronga: ", final)

def max_combination(tab, d, x):
    pass
    # maxim = pow(10, d)
    # count = 0
    # for i in range(4, 10):
    #     if tab[i+1] * d > maxim:
    #         s = tab[i] * d
    #         while s < maxim:
    #             count += 1
    #             s = s - tab[i] + tab[i+1]
    #         result = [0 for j in range(x)]
    #         for j in range(x-1, x-count-1, -1):
    #             result[j] = i + 1
    #         for j in range(x-count-1, x-d-1, -1):
    #             result[j] = i
    #         return result
    # result = [0 for i in range(x)]
    # for i in range(x-1, x-1-d, -1):
    #     result[i] = 3
    # return result


def check_if_armstrong(s, a, d, x):
    tab = [0 for i in range(10)]
    if s < 10 and d == 1:
        return True
    else:
        while s > 0:
            tab[s % 10] += 1
            s //= 10
        for i in range(x-d, x):
            tab[a[i]] -= 1
        for i in range(0, 10):
            if tab[i] != 0:
                return False
    return True

start_time = time.time()
combinations(13)
print("--- %s seconds ---" % (time.time() - start_time))
