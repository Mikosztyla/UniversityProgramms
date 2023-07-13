import math

from kol2atesty import runtests
from math import inf


def drivers( P, B ):
    stop_points = []
    for i in range(len(P)):
        index, control = P[i]
        if control:
            stop_points.append([index, control, i])
    stop_points.sort()
    p_copy = P.copy()
    p_copy.sort()
    it = 0
    cnt = 0

    for index, control in p_copy:
        if control:
            stop_points[it].append(cnt)
            it += 1
        else:
            cnt += 1

    stop_points_number = len(stop_points)
    jacek_min = [inf for _ in range(stop_points_number + 1)]
    marian_min = [inf for _ in range(stop_points_number + 1)]
    result_jacek = [[] for _ in range(stop_points_number + 1)]
    result_marian = [[] for _ in range(stop_points_number + 1)]
    jacek_min[0] = 0
    marian_min[0] = 0

    for i in range(stop_points_number):
        index, control, real_index, temp = stop_points[i]
        cnt = 0
        for j in range(i, i-3, -1):
            if j >= 0:
                if marian_min[j] < jacek_min[i+1]:
                    jacek_min[i+1] = marian_min[j]
                    result_jacek[i+1] = result_marian[j] + [real_index]
                if i >= 1 and j > 0:
                    if jacek_min[j] + index - stop_points[j-1][0] - cnt - 1 < marian_min[i+1]:
                        # marian_min[i+1] = jacek_min[j] + index - stop_points[j-1][0] - cnt - 1
                        marian_min[i + 1] = stop_points[i][3] - stop_points[j-1][3] + jacek_min[j]
                        result_marian[i+1] = result_jacek[j] + [real_index]
            cnt += 1

    result = []
    if jacek_min[-1] < marian_min[-1]:
        result = result_jacek[-1]
    else:
        result = result_marian[-1]
    result.pop(-1)
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )