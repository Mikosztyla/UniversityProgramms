tab = [10, 20, 1, 345, 0, 9, 6, 1, 13]
n = len(tab)

result = 0
for i in range(n):
    suma = tab[i]
    sum_iter = i
    if suma == sum_iter:
        result = max(result, 1)
    for j in range(i+1, n):
        sum_iter += j
        suma += tab[j]
        if suma == sum_iter:
            result = max(result, j-i+1)

print(result)