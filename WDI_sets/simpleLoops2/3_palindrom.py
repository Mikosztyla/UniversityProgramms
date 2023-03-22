# Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

def if_palindrom(n, s):
    x = n
    rev = 0
    while x > 0:
        rev = rev * s + x % s
        x //= s
    if rev == n:
        return True
    else:
        return False


n = int(input())
print(f"Czy liczba {n} jest palindromem w systemie 10: ", if_palindrom(n, 10))
print(f"Czy liczba {n} jest palindromem w systemie 2: ", if_palindrom(n, 2))

# a = "1234"
# a = a[::-1]
# print(a)