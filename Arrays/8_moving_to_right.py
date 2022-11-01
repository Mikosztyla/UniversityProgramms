import random


def check_tab(tab, n):
    flag = [False for _ in range(n)]
    flag[0] = True
    for i in range(n):
        if flag[i]:
            temp = tab[i]
            divisor = 2
            while temp > 1:
                while temp % divisor == 0:
                    temp //= divisor
                    if i + divisor < n:
                        flag[i + divisor] = True
                divisor += 1
    return flag[n-1]


n = int(input("Podaj zakres: "))
tab = [random.randint(1, 100) for _ in range(n)]
print(tab)

print(check_tab(tab, n))
