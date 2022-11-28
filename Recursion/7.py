# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy
# jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.

def szalka(T, n, p):
    if n == 0:
        return True
    if p == len(T):
        return False
    return szalka(T, n, p+1) or szalka(T, n-T[p], p+1)


tab = [4, 5, 6]
print(szalka(tab, 7, 0))