from zad9testy import runtests
from queue import PriorityQueue


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

        no_exceeding = get_min_value(min_cost_of_no_exceeding, curr_station_id - T)
        costs[i][0] = no_exceeding + curr_station_cost
        min_cost_of_no_exceeding.put((costs[i][0], curr_station_id))
        min_cost_of_no_exceeding_2.put((costs[i][0], curr_station_id))

        exceeded = get_min_value(min_cost_exceeded, curr_station_id - T)
        one_exceeding = get_min_value(min_cost_with_one_exceeding, curr_station_id - T)
        costs[i][1] = min(exceeded, one_exceeding) + curr_station_cost
        min_cost_with_one_exceeding.put((costs[i][1], curr_station_id))

    return min(costs[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
