def bubble_sort(tab):
    s = 1
    while s:
        s = 0
        for i in range(1, len(tab)):
            if tab[i] < tab[i-1]:
                tab[i], tab[i-1] = tab[i-1], tab[i]
                s = 1
    return tab


def bucket_sort(tab):
    buckets = [[] for _ in range(10)]
    for i in range(len(tab)):
        buckets[tab[i]//10] += [tab[i]]
    result_tab = []
    for i in range(10):
        if len(buckets[i]) > 1:
            buckets[i] = bubble_sort(buckets[i])
            result_tab += buckets[i]
    return result_tab


T = [2, 65, 8, 34, 19, 99, 40, 63, 3, 34, 15, 14, 13, 12, 76, 85, 56, 90, 45, 67, 98, 99, 98, 99, 0]
T = bucket_sort(T)
print(T)