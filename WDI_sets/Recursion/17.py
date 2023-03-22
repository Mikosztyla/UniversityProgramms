# Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
# wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
import math


def build_numbers(num1, num2, it_1, it_2, curr_num, take_first_num):
    if take_first_num:
        curr_num = curr_num*10 + int(num1 // 10**(it_1-1))
        num1 %= 10**(it_1-1)
        it_1 -= 1
    else:
        curr_num = curr_num*10 + int(num2 // 10**(it_2-1))
        num2 %= 10**(it_2-1)
        it_2 -= 1
    if it_1 > 0:
        build_numbers(num1, num2, it_1, it_2, curr_num, True)
    if it_2 > 0:
        build_numbers(num1, num2, it_1, it_2, curr_num, False)
    if it_1 == 0 and it_2 == 0:
        print(curr_num)


num1 = 123
num2 = 45
l1 = int(math.log10(num1)) + 1
l2 = int(math.log10(num2)) + 1
build_numbers(num1, num2, l1, l2, 0, True)
build_numbers(num1, num2, l1, l2, 0, False)