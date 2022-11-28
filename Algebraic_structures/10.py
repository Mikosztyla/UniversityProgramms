# Zadanie 10. Proszę napisać funkcję która zamienia liczby wymierne reprezentowane
# jako rozwinięcia dziesiętne w postaci napisów na liczbę w postaci pary licznik
# mianownik. Na przykład: ”0.25” na (1,4), ”0.1(6)” na (2,3), ”0.(142857)” na (1,7)


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(a, b):
    return (a*b)//nwd(a, b)


def dodawanie(a, b, c, d):
    if a == 0 and b == 0:
        return c, d
    return a * nww(b, d)//b + c * nww(b, d)//d, nww(b, d)


def skroc(a, b):
    return a//nwd(a, b), b//nwd(a, b)


test = "0.1(6)"
pos_point = test.find(".")
pos_bracket = test.find("(")
l = m = 1
a = b = c = d = 0
e, f = 1, 1
if pos_point != -1:
    l = int(test[0:pos_point])

    if pos_bracket-pos_point > 1:
        a = int(test[pos_point+1:pos_bracket])
        b = 10**(pos_bracket-pos_point-1)
    if pos_bracket > -1:
        temp = test[pos_bracket + 1:test.find(")")]
        c = int(temp)
        if b == 0:
            d = ((10 ** len(temp)) - 1)
        else:
            d = ((10 ** len(temp)) - 1) * b

        e, f = dodawanie(a, b, c, d)
        l, m = dodawanie(l, m, e, f)
    else:
        a = int(test[pos_point+1:])
        b = 10**(len(test[pos_point+1:]))
        l, m = dodawanie(l, m, a, b)
else:
    l = int(test)

print(skroc(l, m))
