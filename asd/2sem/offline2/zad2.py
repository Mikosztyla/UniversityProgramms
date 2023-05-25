# Mikołaj Gosztyła
# Mój algorytm będzie wybierał po kolei największe wartości z danej tablicy "S" za pomocą kopca wykorzystywanego w
# sortowaniu "heapsort". Algorytm będzie działał, aż liczba dni nie przekroczy największej pozostałej wartości
# w kopcu (jeśli liczba dni przekroczy tę wartość, to nie damy rady już wziąć więcej śniegu, ponieważ zdąży już
# stopnieć). Algorytm będzie działał poprawnie, ponieważ najbardziej obfite w śnieg obszary są najbardziej opłacalne,
# a kolejność ich zbierania nie ma znaczenia (całkowita suma wybranych do zebrania obszarów śniegu jest zawsze taka
# sama i zawsze zbieranie zajmie nam to tyle samo dni, więc niezależnie od ustawienia obszarów, zawsze zbierzemy tyle
# samo, np. zbierając od lewej do prawej strony, nie pomijając żadnego obszaru). Oznacza to, że po wybraniu które
# obszary śniegu zbierzemy, możemy je zebrać np. od lewej strony do prawej, względem ich początkowego ustawienia i
# algorytm zwróci poprawny wynik.
from zad2testy import runtests


def heapify(tab, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_i = i
    if l < n and tab[l] > tab[max_i]:
        max_i = l
    if r < n and tab[r] > tab[max_i]:
        max_i = r

    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def snow( S ):
    result = index = 0
    n = len(S)
    for i in range((n - 2) // 2, -1, -1):
        heapify(S, i, n)
    curr_i = n-1
    while S[0] - index > 0 and curr_i >= 0:
        result += S[0] - index
        index += 1
        S[0], S[curr_i] = S[curr_i], S[0]
        heapify(S, 0, curr_i)
        curr_i -= 1
    return result


runtests( snow, all_tests = True )
