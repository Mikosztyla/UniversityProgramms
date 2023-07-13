from egz2btesty import runtests


def magic( C ):
    n = len(C)
    result = [-1 for _ in range(n)]
    result[0] = 0
    for i in range(n-1):
        if result[i] != -1:
            for j in range(1, 4):
                temp = C[i][0] + result[i] - C[i][j][0]
                if temp - result[i] <= 10 and temp >= 0 and C[i][j][1] != -1:
                    if result[C[i][j][1]] < temp:
                        result[C[i][j][1]] = temp
    return result[-1]


runtests( magic, all_tests = True )
