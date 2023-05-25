# liczby z przedziału 0 <= Ti <= n^2-1

def change(x, n, i):
    if i == 1:
        return x % n
    else:
        return (x // n) % n


def counting_sort(T, n, i):
    tmp = [0 for _ in range(n)]
    t2 = [0 for _ in range(n)]
    x = len(T)
    for j in range(x):
        tmp[change(T[j], n, i)] += 1
    for j in range(1, x):
        tmp[j] += tmp[j-1]
    for j in range(x-1, -1, -1):
        t2[tmp[change(T[j], n, i)]-1] = T[j]
        tmp[change(T[j], n, i)] -= 1
    return t2


def radix_sort(T):
    n = len(T)
    for i in range(1, 3):
        T = counting_sort(T, n, i)
    return T


T = [99, 54, 36, 42, 47, 4, 3, 6, 6, 3]
T = radix_sort(T)
print(T)

# najkrótszy podciąg zaweirający wszystkie kolory
