from egz2atesty import runtests
from queue import PriorityQueue


def coal(A, T):
    stores = []
    last_store = 0;
    for c in A:
        index = 0
        while index < len(stores) and c > 0:
            if stores[index] >= c:
                stores[index] -= c
                c = 0
                last_store = index
            index += 1
        if c > 0:
            stores.append(T)
            stores[index] -= c
            last_store = index
    return last_store


def coal2(A, T):
    queue = PriorityQueue()



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
