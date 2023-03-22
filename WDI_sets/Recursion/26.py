# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)
def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    a = 5
    while a < int(x**0.5) + 1:
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
    return True


def check_if_prime(T):
    mult = 1
    result = 0
    for i in range(len(T)-1, -1, -1):
        result += T[i] * mult
        mult *= 2
    return is_prime(result)


def get_binary_numbers(a, b, number=[1]):
    if a == 0 and b == 0:
        if number[-1] == 1:
            if check_if_prime(number):
                print(number, "pierwsza")
                return
        global licznik
        licznik += 1
        print(number)
    if a > 0:
        get_binary_numbers(a-1, b, number + [1])
    if b > 0:
        get_binary_numbers(a, b-1, number + [0])
    return


a = 2
b = 3
licznik = 0
get_binary_numbers(a-1, b)
print(licznik)