# Dana jest tablica T zawierająca ciąg liczb naturalnych. Maksymalny, spójny podciąg rosnący
# to taki, w którym przed pierwszym elementem nie ma elementu mniejszego, a za ostatnim elementem
# nie ma elementu większego. Proszę napisać funkcję sequence(T) która sprawdza czy w tablicy można
# znaleźć dwa maksymalne, spójne podciągi rosnące, każdy o długości większej od 2, takie, aby po
# ich złączeniu staoiwły jeden ciąg rosnący. Funkcja powinna zwrócić wartość True albo False
def sequence(T):
    l = len(T)
    max_first = 0
    min_last = -1
    length = 1
    first = T[0]
    for i in range(1, l):
        if T[i] > T[i-1]:
            length += 1
        else:
            if length > 2:
                if T[i-1] < max_first or (min_last != -1 and first > min_last):
                    return True
                else:
                    if first > max_first:
                        max_first = first
                    if min_last == -1:
                        min_last = T[i-1]
                    elif T[i-1] < min_last:
                        min_last = T[i-1]
            length = 1
            first = T[i]
    return False


print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]))
