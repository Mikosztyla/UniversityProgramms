
for i in range(1, 100):
    for j in range(1, 100):
        a, b = i, j
        while a < 2030:
            if a == 2022:
                print("jooooo")
                print(i, j)
            a, b = b, a+b

#57 -> min, a = 53, b = 4