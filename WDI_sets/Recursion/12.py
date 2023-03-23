# Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
# Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.

def enki(T, s, n, p, res):
    global licznik
    if n == 1:
        for i in range(p, len(T)):
            if s == T[i]:
                licznik += 1
                print(res + [T[i]])
    else:
        for i in range(p, len(T)):
            if s % T[i] == 0:
                enki(T, s//T[i], n-1, i+1, res + [T[i]])


licznik = 0
tab = [1, 2, 3, 4, 5, 6, 12]
enki(tab, 24, 4, 0, [])
print(licznik)