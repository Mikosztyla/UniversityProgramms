# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy
# jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach
# Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

def dwie_szalki(T, n, p, res):
    if n == 0:
        return res
    if p == len(T):
        return None
    return dwie_szalki(T, n, p+1, res) or dwie_szalki(T, n-T[p], p+1, res + [-T[p]]) or dwie_szalki(T, n+T[p], p+1, res + [T[p]])


tab = [1, 2, 10]
result = dwie_szalki(tab, 8, 0, [])
print(result)