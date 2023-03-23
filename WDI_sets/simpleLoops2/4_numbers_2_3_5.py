# Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.

n = int(input())

i = j = k = 1
s = 0
while i <= n:
    j = i
    while j <= n:
        k = j
        while k <= n:
            s += 1
            k *= 5
        j *= 3
    i *= 2
print(s)
