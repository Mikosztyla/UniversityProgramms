

def fill_tab(a, b, tab):
    for i in range(1, n):
        a *= 10
        tab[i] += a // b
        a %= b
        if a == b:
            return


def correct_tab(tab, n):
    for i in range(n-1, 0, -1):
        if tab[i] >= 10:
            tab[i-1] += tab[i] // 10
            tab[i] %= 10


n = int(input("Ile ma byc cyfr po przecinku: "))
tab = [0 for _ in range(n)]
tab[0] = 2
fact = 2
m = 2
while fact < 10**n:
    fill_tab(1, fact, tab)
    correct_tab(tab, n)
    m += 1
    fact *= m

print(tab[0], end="")
print(",", end="")
for i in range(1, n):
    print(tab[i], end="")