# Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę
# składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.


# def rozloz(num, curr_num, res):
#     if curr_num == 0:
#         return
#     for el in res:
#         print(el, "+", end=" ")
#     print(curr_num)
#     rozloz(num, curr_num-1, res+[1])
#     #rozloz(curr_num, curr_num-1, res=[num-curr_num])
#
#
# def rozloz2(num, curr_num, res):
#     print(res[0], end="")
#     curr_num += res[0]
#     if len(res) > 1:
#         for i in range(1, len(res)):
#             curr_num += res[i]
#             print(" +", res[i], end="")
#     while curr_num < num:
#         curr_num += 1
#         print(" + 1", end="")
#         res += [1]
#     if len(res) > 1:
#         while len(res) > 0 and res[-1] == 1:
#             res = res[:-1]
#     if len(res) == 1:
#         res[0] -= 1
#         if res[0] > 0:
#             suma = res[0]
#             first = res[0]
#             while num >= suma + first:
#                 res = res + [first]
#                 suma += first
#             first -= 1
#             while first > 1:
#                 while suma + first <= num:
#                     res = res + [first]
#                     suma += first
#                 first -= 1
#             print()
#             rozloz2(num, 0, res)
#     elif len(res) == 0:
#         return
#     else:
#         print()
#         res[-1] -= 1
#         rozloz2(num, 0, res)

def f(n):
    parts=[]

    def rec(n,maxi=n,t=[]):
        nonlocal parts
        if n==0:
            parts+=[t]
            return

        for i in range(1,min(n,maxi)+1):
            rec(n-i,i,t+[i])

    rec(n)
    print(parts)

f(4)

# rozloz2(10, 0, [10])