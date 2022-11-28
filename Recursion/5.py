# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    a = 5
    while a < (x**.5 + 1):
        if x % a == 0:
            return False
        a += 2
        if x % a == 0:
            return False
        a += 4
    return True


def get_primes(T, p):
    number = 0
    result = False
    i = p
    while i <= len(T) and not result:
        while not is_prime(number) and i < len(T):
            if T[i] == 0:
                number *= 2
            elif T[i] == 1:
                number = number * 2 + 1
            i += 1
        if i == len(T) and is_prime(number):
            return True
        elif is_prime(number):
            result = get_primes(T, i)
        elif i == len(T):
            return False

        if not result:
            if T[i] == 0:
                number *= 2
            elif T[i] == 1:
                number = number * 2 + 1
            i += 1
    return result


print(get_primes([1, 1, 0, 1, 0, 0, 1], 0))