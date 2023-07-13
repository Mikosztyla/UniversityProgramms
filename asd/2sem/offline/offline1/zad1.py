# Mikołaj Gosztyła
# Mój algorytm będzie iterował po każdej literze w słowie "s", traktując zmienną "i" jako indeks litery z prawej
# części palindromu. Algorytm ten stwierdza istnienie palindromu na podstawie równości litery o indeksie "i" z literą
# o odpowiednim indeksie z lewej części palindromu. Zapamięta on również pozycje początku palindromu, którego mógł
# pominąć podczas iteracji po aktualnie sprawdzanym palindromie i wróci do tej pozycji. Tym samym sprawdzi on długość
# wszystkich palindromów występujących w słowie "s", wybierając najdłuższą z nich.
# Algorytm posiada złożoność O(n) przy pozytywnym przypadku i O(n^2) przy negatywnym przypadku.

from zad1testy import runtests


def ceasar(s):
    max_result = 1
    result = 1
    diff = 2
    i = 0
    l = len(s)
    rem_i = -1
    while i < l:
        if i - diff >= 0 and s[i] == s[i - diff]:
            if rem_i == -1 and diff != 2 and s[i] == s[i - 2]:
                rem_i = i
            result += 2
            diff += 2
            i += 1
        else:
            if diff == 2:
                i += 1
            max_result = max(result, max_result)
            if l - max_result//2 < i:
                i = l
                rem_i = -1
            diff = 2
            result = 1
            if rem_i != -1:
                i = rem_i
                rem_i = -1
    return max(result, max_result)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
