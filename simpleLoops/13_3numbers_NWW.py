def nww(a, b):
    return a * b // nwd(a, b)


def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a = 60
b = 40
c = 43
nww_abc = nww(nww(a, b), c)
print(nww_abc)