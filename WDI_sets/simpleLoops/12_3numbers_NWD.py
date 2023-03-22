# Zadanie 12. Prosze napisac program wyznaczajacy najwiekszy wspólny dzielnik 3 zadanych liczb.

def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a = 80
b = 40
c = 120
nwd_abc = nwd(nwd(a, b), c)
print(nwd_abc)