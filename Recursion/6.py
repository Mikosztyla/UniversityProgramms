# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

def znajdz_sume_podciagu(T, suma_el=0, suma_i=0, ilosc_el=1, p=0):
    naj_suma = 0
    naj_el = 0
    for i in range(p, len(T)):
        suma_el += T[i]
        suma_i += i
        if suma_el == suma_i:
            return suma_el, ilosc_el
        suma, ilosc = znajdz_sume_podciagu(T, suma_el, suma_i, ilosc_el+1, i+1)
        #to zwraca sumę 10
        # ----------------
        # if ilosc > 0:
        #     naj_el = ilosc
        #     naj_suma = suma
        # ----------------
        # to zwraca sumę 8
        # ----------------
        if (naj_suma == 0 and naj_el == 0) or (suma < naj_suma and ilosc < naj_el):
            if ilosc != 0:
                naj_suma = suma
                naj_el = ilosc
        # ----------------
        suma_el -= T[i]
        suma_i -= i
    return naj_suma, naj_el


print(znajdz_sume_podciagu([1, 7, 3, 5, 11, 2]))

