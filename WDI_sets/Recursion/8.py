# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy
# jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach

def dwie_szalki(T, n, p):
    if n == 0:
        return True
    if p == len(T):
        return False
    return dwie_szalki(T, n, p+1) or dwie_szalki(T, n-T[p], p+1) or dwie_szalki(T, n+T[p], p+1)


tab = [1, 2, 10]
print(dwie_szalki(tab, 6, 0))