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
    # t = [[0 for j in range(x)] for i in range(10)]
    # print(t)
    zbior = [0 for i in range(x)]
    j = x-1
    s = 0
    digits = 1
    while True:
        s += 1
        for i in range(x-1, x-1-digits, -1):
            print(zbior[i], end="")
        print()
        if zbior[x-1] < 9:
            j = x - 1
            zbior[j] += 1
        else:
            j = x - 2
            while j >= 0 and zbior[j] == zbior[j+1]:
                j -= 1
            if j >= 0:
                if zbior[j] == 0:
                    digits += 1
                zbior[j] += 1
                for k in range(j, x-1):
                    zbior[k+1] = zbior[k]
        if j < 0:
            break
    print("Liczba kombinacji: ", s)


combinations(3)