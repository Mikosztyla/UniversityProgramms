# Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi wież, pierwsza wieża
# startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu dzachownicy. Pierwsza wieża może wykonywać tyrlko
# ruchy w prawo lub w dół szachownicy. Druga wieża startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu
# szachownicy. Druga wieża może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
# w mniejszej liczby ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wetedy. Gdy liczby na obu polach są
# względnie pierwsze. Proszę napisać funkcję. która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0 jeżeli
# wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym polu. Po wykonaniu
# funkcji zawartość tablicy nie może ulec zmienia.
import random


def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_path(tab, start_w, start_k, finish_w, finish_k, m=0, is_left=True):
    if start_w == finish_w and start_k == finish_k:
        return m
    m1 = m2 = -1

    for i in range(start_w+1, len(tab)):
        if nwd(tab[i][start_k], tab[start_w][start_k]) == 1:
            temp = get_path(tab, i, start_k, finish_w, finish_k, m+1, is_left)
            if temp != -1:
                m1 = temp
    if is_left:
        for j in range(start_k+1, len(tab)):
            if nwd(tab[start_w][j], tab[start_w][start_k]) == 1:
                temp = get_path(tab, start_w, j, finish_w, finish_k, m+1, is_left)
                if temp != -1:
                    m2 = temp
    else:
        for j in range(start_k-1, -1, -1):
            if nwd(tab[start_w][j], tab[start_w][start_k]) == 1:
                temp = get_path(tab, start_w, j, finish_w, finish_k, m + 1, is_left)
                if temp != -1:
                    m2 = temp

    if m1 == -1:
        return m2
    if m2 == -1:
        return m1
    return min(m1, m2)


#tab = [[random.randint(1, 20) for _ in range(8)] for _ in range(8)]
tab = [
[2, 20, 1, 4, 19, 5, 9, 20],
[2, 2, 13, 1, 6, 16, 12, 11],
[2, 1, 3, 9, 13, 10, 12, 18],
[2, 8, 15, 2, 5, 13, 20, 12],
[2, 1, 8, 3, 3, 1, 2, 3],
[9, 3, 3, 3, 3, 3, 3, 7],
[3, 3, 3, 3, 3, 3, 3, 3],
[2, 2, 2, 2, 2, 2, 2, 2]
]
# tab = [
# [2, 20, 5, 9, 20],
# [9, 2, 16, 12, 11],
# [10, 1, 3, 12, 18],
# [15, 8, 13, 20, 12],
# [8, 1, 1, 2, 3]
# ]
for i in range(len(tab)):
    print(tab[i])
print(get_path(tab, 0, 0, len(tab)-1, len(tab)-1, 0, True))
print(get_path(tab, 0, len(tab)-1, len(tab)-1, 0, 0, False))