tab = [6, 2, 8, 3, 5, 1, 3, 2, 7, 5, 4, 6]

s = True
while s:
    s = False
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            tab[i], tab[i+1] = tab[i+1], tab[i]
            s = True
print(tab)