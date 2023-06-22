from zad9testy import runtests
import copy
from queue import PriorityQueue


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(tab, i, n):
    if i < n:
        l = left(i)
        r = right(i)
        max_i = i

        if l < n and tab[l][0] < tab[max_i][0]:
            max_i = l
        if r < n and tab[r][0] < tab[max_i][0]:
            max_i = r

        if max_i != i:
            tab[i], tab[max_i] = tab[max_i], tab[i]
            heapify(tab, max_i, n)


def build_heap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)


def heapsort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)


def count_curr_min_cost(tab, costs, i, index, curr_station_id, r):
    min_index = curr_station_id - r
    if len(tab) > 0:
        tab_copy = copy.deepcopy(tab)
        while tab[0][1] < min_index or tab[0][1] == curr_station_id:
            tab[0], tab[-1] = tab[-1], tab[0]
            tab.pop(-1)
            heapify(tab, 0, len(tab))

        costs[i][index] = tab[0][0]
        return tab_copy


def clear_heap(tab, r):
    while len(tab) > 0 and tab[0][1] < r:
        tab[0], tab[-1] = tab[-1], tab[0]
        tab.pop(-1)
        heapify(tab, 0, len(tab))


def repair_heap(tab):
    n = len(tab)
    p = parent(n-1)
    curr_i = n-1
    while tab[p][0] > tab[curr_i][0]:
        tab[p], tab[curr_i] = tab[curr_i], tab[p]
        curr_i = p
        p = parent(curr_i)


def get_min_value(queue, r):
    curr_val, curr_id = queue.get()
    while curr_id < r:
        curr_val, curr_id = queue.get()
    queue.put((curr_val, curr_id))
    return curr_val


def min_cost( O, C, T, L ):
    n = len(C)
    stations = [(0, 0) for _ in range(n)]

    for i in range(n):
        stations[i] = (O[i], C[i])
    stations.sort()
    stations.append((L, 0))
    costs = [[0, 0, 0] for _ in range(n + 1)]
    min_cost_of_no_exceeding = PriorityQueue()
    min_cost_of_no_exceeding_2 = PriorityQueue()
    min_cost_with_one_exceeding = PriorityQueue()
    min_cost_exceeded = PriorityQueue()
    min_cost_of_no_exceeding_2.put((0, 0))
    min_cost_with_one_exceeding.put((0, 0))
    min_cost_of_no_exceeding.put((0, 0))
    min_cost_exceeded.put((0, 0))
    for i in range(n + 1):
        curr_station_id, curr_station_cost = stations[i]

        no_exceeding = get_min_value(min_cost_of_no_exceeding_2, curr_station_id - 2 * T)
        costs[i][2] = no_exceeding + curr_station_cost
        min_cost_exceeded.put((costs[i][2], curr_station_id))

        # temp = PriorityQueue()
        # temp.queue = copy.deepcopy(min_cost_of_no_exceeding.queue)
        no_exceeding = get_min_value(min_cost_of_no_exceeding, curr_station_id - T)
        costs[i][0] = no_exceeding + curr_station_cost
        # min_cost_of_no_exceeding.queue = copy.deepcopy(temp.queue)
        min_cost_of_no_exceeding.put((costs[i][0], curr_station_id))
        min_cost_of_no_exceeding_2.put((costs[i][0], curr_station_id))

        exceeded = get_min_value(min_cost_exceeded, curr_station_id - T)
        one_exceeding = get_min_value(min_cost_with_one_exceeding, curr_station_id - T)
        costs[i][1] = min(exceeded, one_exceeding) + curr_station_cost
        min_cost_with_one_exceeding.put((costs[i][1], curr_station_id))

    return min(costs[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
