# Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

def macierz(T):
    result = 0
    if len(T) == 1:
        return T[0]
    elif len(T) == 2:
        return T[0][0] * T[1][1] - T[1][0] * T[0][1]
    else:
        for i in range(len(T)):
            temp = [[0 for _ in range(len(T)-1)] for _ in range(len(T)-1)]
            iterator = 0
            for j in range(len(T)):
                if j != i:
                    for k in range(len(T)-1):
                        temp[iterator][k] = T[j][k+1]
                    iterator += 1
            result += (-1)**i * T[i][0] * macierz(temp)
    return result


tab = [[2, 7, -1, 3, 2], [0, 0, 1, 0, 1], [-2, 0, 7, 0, 2], [-3, -2, 4, 5, 3], [1, 0, 0, 0, 1]]
print(macierz(tab))