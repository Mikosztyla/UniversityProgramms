class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def makeLinkedList(tab):
    start = Node(tab[0])
    k = start
    for i in range(1, len(tab), 1):
        k.next = Node(tab[i])
        k = k.next
    return start


def insert(p, number):
    if p is None:
        return number
    k = p
    s = None
    while k and k.value < number.value:
        s = k
        k = k.next
    if s is None:
        number.next = p
        p = number
        return p
    s.next = number
    number.next = k
    return p


def deleteMaxFromList(p):
    maxNode = p
    sMaxNode = None
    k = p
    s = None
    while k:
        if k.value > maxNode.value:
            maxNode = k
            sMaxNode = s
        s = k
        k = k.next
    if sMaxNode is None:
        p = maxNode.next
        maxNode.next = None
        return p, maxNode
    sMaxNode.next = maxNode.next
    maxNode.next = None
    return p, maxNode


def printList(p):
    while p:
        print(p.value, end=" ")
        p = p.next
    print()


tab = [1, 3, 5, 6, 7, 8, 9, 13, 15, 35, 46, 57]
# p = makeLinkedList(tab)
# printList(p)
# p = insert(p, Node(60))
# print()
# printList(p)
tab2 = [6000, 8, 6, 34, 12, 77, 6, 455]
p = makeLinkedList(tab2)
sorted = None
while p:
    p, k = deleteMaxFromList(p)
    sorted = insert(sorted, k)
printList(sorted)