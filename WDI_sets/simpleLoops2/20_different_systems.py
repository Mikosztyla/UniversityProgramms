# Zadanie 20. Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę
# napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
# 2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).

def is_different(a, b, s):
    digits = [0 for i in range(s)]
    while a > 0:
        digits[a % s] += 1
        a //= s
    while b > 0:
        if digits[b % s] != 0:
            return False
        b //= s
    return True


a = 123
b = 522

for i in range(2, 17):
    if is_different(a, b, i):
        print(i)
        break
else:
    print("Nie istnieje taka podstawa")