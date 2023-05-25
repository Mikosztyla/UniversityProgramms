class Node():
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


def tab_to_list(tab):
    p = Node(tab[0])
    k = p
    for i in range(1, len(tab)):
        k.next = (Node(tab[i]))
        k = k.next
    return p


def list_to_tab(p):
    tab = []
    while p:
        tab.append(p.value)
        p = p.next
    return tab


def heapify(tab, i, n):
    l = 2*i + 1
    r = 2*i + 2
    max_i = i
    if l < n and tab[l] < tab[max_i]:
        max_i = l
    if r < n and tab[r] < tab[max_i]:
        max_i = r
    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def build_heap(tab, n):
    for i in range((n-2)//2, -1, -1):
        heapify(tab, i, n)


def sort_h(p, k):
    tab = list_to_tab(p)
    n = len(tab)
    temp = [0 for _ in range(k+1)]
    for i in range(k+1):
        temp[i] = tab[i]
    build_heap(temp, k+1)
    it = k + 1
    l = len(temp)
    for i in range(n):
        tab[i] = temp[0]
        if it < n:
            temp[0] = tab[it]
            it += 1
        else:
            l -= 1
            temp[0] = temp[l]
        heapify(temp, 0, l)
    return tab


T = [1, 0, 3, 2, 4, 6, 5]
p = tab_to_list(T)
T = sort_h(p, 1)
print(T)