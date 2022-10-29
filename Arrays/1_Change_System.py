def change_system(x, s):
    t = [0 for i in range(64)]
    iterator = 0
    while x > 0:
        t[iterator] = x % s
        x //= s
        iterator += 1

    for i in range(iterator-1, -1, -1):
        print("0123456789ABCDEF"[t[i]], end="")


n = int(input("Podaj liczbe: "))

for i in range(2, 17):
    print(f"Licza {n} w systemie {i} to: ", end="")
    change_system(n, i)
    print()