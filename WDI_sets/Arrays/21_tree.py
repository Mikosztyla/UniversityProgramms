# Zadanie 21. Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
# zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek.
def nwd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def trojki():
    masks = [3, 5, 6, 10]
    s = 0
    for i in range(n - 2):
        for j in masks:
            t = [tab[i], 0, 0]
            t_it = 1
            tab_it = i + 1
            while j > 0:
                if j % 2 == 1:
                    if t_it > n - 1 or tab_it > n - 1:
                        break
                    t[t_it] = tab[tab_it]
                    t_it += 1
                j //= 2
                tab_it += 1
            else:
                if nwd(nwd(t[0], t[1]), t[2]) == 1:
                    print(t[0], t[1], t[2])
                    s += 1
    return s


tab = [1, 6, 4, 2, 8, 9, 7, 3, 11, 13, 16]
print(tab)
n = len(tab)
print("Trojek jest:", trojki())