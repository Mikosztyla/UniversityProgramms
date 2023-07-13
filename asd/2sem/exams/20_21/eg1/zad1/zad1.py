from zad1testy import runtests
from queue import PriorityQueue


def chaos_index(T):
    queue = PriorityQueue()
    n = len(T)
    for i in range(n):
        queue.put((T[i], i))

    max_difference = 0
    for i in range(n):
        val, index = queue.get()
        if abs(i - index) > max_difference:
            max_difference = abs(i-index)
    return max_difference


runtests( chaos_index )
