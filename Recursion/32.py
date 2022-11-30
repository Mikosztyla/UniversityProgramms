# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

def check_tab(T, k, suma1=0, suma2=0, k1=0, k2=0, p=0):
    if k1 == k2 == k and suma1 == suma2:
        return True
    if p == len(T):
        return False
    for i in range(p, len(T)):
        if check_tab(T, k, suma1+T[i], suma2, k1+1, k2, i+1):
            print(T[i])
            return True
        if check_tab(T, k, suma1, suma2+T[i], k1, k2+1, i+1):
            print("-", T[i])
            return True
        if check_tab(T, k, suma1, suma2, k1, k2, i+1):
            return True
    return False


print(check_tab([1, 2, 345, 34, 7, 0, 7, 8, 3], 3))