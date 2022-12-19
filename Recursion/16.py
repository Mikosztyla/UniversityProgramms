# Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz
# sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ula → 117, 108, 97
# oraz exe → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z
# podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
# znaleziony wyraz.

def ile_samoglosek(s):
    licznik = 0
    suma_asci = 0
    for litera in s:
        if ord(litera) == 97 or ord(litera) == 101 or ord(litera) == 105 or ord(litera) == 111 or ord(litera) == 117:
            licznik += 1
        suma_asci += ord(litera)
    return licznik, suma_asci


def wyraz(s1, s2):
    print(s1, s2)
    samogloski1, waga1 = ile_samoglosek(s1)

    def sprawdz(s, current_s, p):
        nonlocal samogloski1, waga1
        samogloski2, waga2 = ile_samoglosek(current_s)
        if samogloski2 == samogloski1 and waga2 == waga1:
            print(current_s)
            return True

        for i in range(p, len(s)):
            if sprawdz(s, current_s + s[i], i+1):
                return True
        return False

    return sprawdz(s2, "", 0)


print(wyraz("ula", "ekkasdsxgarsssse"))

