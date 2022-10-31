import random
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def check_sum(comb, sums, t1, t2):
    s = 0
    iterator = 0
    for i in comb:
        s += sums[iterator + i -1]
        iterator += 3
    if is_prime(s):
        iterator = 0
        for i in comb:
            if i == 1:
                print(t1[iterator], end=" ")
            elif i == 2:
                print(t2[iterator], end=" ")
            else:
                print(f"{t1[iterator]} + {t2[iterator]}", end=" ")
            iterator += 1
            if iterator < n:
                print("+ ", end="")
        print(f"= {s}")


def find_sums(t1, t2):
    comb = [1 for _ in range(n)]
    while True:
        check_sum(comb, sums, t1, t2)
        if comb[n - 1] < 3:
            j = n - 1
            comb[j] += 1
        else:
            j = n - 2
            while j >= 0 and comb[j] == comb[j + 1]:
                j -= 1
            if j >= 0:
                comb[j] += 1
                for i in range(j + 1, n):
                    comb[i] = 1
        if j < 0:
            break


n = int(input("Podaj zakres: "))
t1 = [random.randint(1, 10) for _ in range(n)]
t2 = [random.randint(1, 10) for _ in range(n)]
print(t1)
print(t2)
sums = [0 for _ in range(n*3)]
for i in range(n):
    temp = 3*i
    sums[temp] = t1[i]
    sums[temp + 1] = t2[i]
    sums[temp + 2] = t1[i] + t2[i]

find_sums(t1, t2)