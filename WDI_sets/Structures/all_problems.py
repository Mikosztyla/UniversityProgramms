class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Node2:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


def tab_to_list(tab):
    p = Node(tab[0])
    r = p
    for i in range(1, len(tab)):
        k = Node(tab[i])
        r.next = k
        r = r.next
    return p


def tab_to_2way_list(tab):
    p = Node2(tab[0])
    if len(tab) == 1:
        return p
    q = p
    k = Node2(tab[1])
    p.next = k
    k.previous = p
    q = k
    for i in range(2, len(tab)):
        k = Node(tab[i])
        q.next = k
        k.previous = q
        q = q.next
    return p


def print_forward(zb):
    while zb:
        if zb.value is not None:
            print(zb.value, end=" ")
        zb = zb.next
    print()
    return


def print_backward(zb):
    if zb:
        print_backward(zb.next)
        print(zb.value, end=" ")
    print()
    return


def scal(p1, p2):
    if not p1 and not p2:
        return None
    if not p1:
        return p2
    if not p2:
        return p1

    q = Node()
    if p1.value < p2.value:
        q = p1
        p1 = p1.next
    else:
        q = p2
        p2 = p2.next

    res = q
    while p1 and p2:
        if p1.value < p2.value:
            q.next = p1
            p1 = p1.next
        else:
            q.next = p2
            p2 = p2.next
        q = q.next
    if p1:
        q.next = p1
    elif p2:
        q.next = p2
    return res


def scal_rec(p1, p2):
    if not p1 and not p2:
        return None
    q = Node()
    if p1.value < p2.value:
        q = p1
        p1 = p1.next
    else:
        q = p2
        p2 = p2.next

    def rec(q, p1, p2):
        if not p1:
            q.next = p2
            return q
        if not p2:
            q.next = p1
            return q
        if p1.value < p2.value:
            q.next = rec(p1, p1.next, p2)
        else:
            q.next = rec(p2, p1, p2.next)
        return q

    return rec(q, p1, p2)


# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.
def p4_reverse(t):
    if not t:
        return None
    q = Node()
    q.value = t.value
    k = Node()
    t = t.next
    while t:
        k = Node(t.value)
        k.next = q
        q = k
        t = t.next
    return q


# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.
def p5_last_didit_list(p):
    tab = [[Node(), Node()] for _ in range(10)]
    for i in range(10):
        tab[i][0] = tab[i][1]
    while p:
        if p.value:
            tab[p.value % 10][1].value = p.value
            tab[p.value % 10][1].next = Node()
            tab[p.value % 10][1] = tab[p.value % 10][1].next
        p = p.next
    q = Node()
    res = q
    for i in range(10):
        print(f"{i}: ", end="")
        print_forward(tab[i][0])
        while tab[i][0]:
            q.value = tab[i][0].value
            q.next = Node()
            q = q.next
            tab[i][0] = tab[i][0].next
    print_forward(res)


# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.
def p8_every_2_deleted(p):
    q = p
    r = p
    while q:
        q = q.next
        if q:
            q = q.next
            r.next = q
            r = r.next
    return p


# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1.
def p9_decrease_number_by_1(p):
    if p is None:
        return
    r = p
    while r.next is not None:
        r = r.next
    r.value -= 1
    return p


# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.
def p10_add_2_numbers(p1, p2):
    if p1 is None and p2 is None:
        return
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    res = Node()
    q = res
    r1 = p4_reverse(p1)
    r2 = p4_reverse(p2)
    rest = 0
    while r1 is not None and r2 is not None:
        curr = rest + r1.value + r2.value
        if curr >= 10:
            rest = 1
            curr -= 10
        else:
            rest = 0
        q.value = curr
        q.next = Node()
        q = q.next
        r1 = r1.next
        r2 = r2.next
    p = Node()
    if r1 is not None:
        p = r1
    else:
        p = r2
    s = q
    while p is not None:
        curr = rest + p.value
        if curr >= 10:
            rest = 1
            curr -= 10
        else:
            rest = 0
        q.value = curr
        q.next = Node()
        q = q.next
        s = q
        p = p.next
    if rest == 1:
        s.next = Node(1)
    res = p4_reverse(res)
    return res


# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.
def p11_add_or_delete(p, el):
    if p is None:
        return
    if el < p.value:
        k = Node(el)
        k.next = p
        return k
    if el == p.value:
        p = p.next
        return p
    s = q = p
    while q is not None and q.value < el:
        s = q
        q = q.next
    if q is None:
        s.next = Node(el)
        return p
    if q.value == el:
        s.next = q.next
        return p
    s.next = Node(el)
    s.next.next = q
    return p


# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.
def p13_delete_lower_numbers(p):
    if p is None:
        return
    s = q = p
    q = q.next
    if q is None:
        return
    last = s.value
    while q is not None:
        if q.value < last:
            last = q.value
            q = q.next
            s.next = q
        else:
            s = q
            q = q.next
            last = s.value
    return p


# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich
# elementów.
def p14_delete_dividable_numbers(p):
    if p is None or p.next is None:
        return
    s = q = p
    q = q.next
    last = q.value
    while q.next is not None:
        if q.next.value % last == 0:
            last = q.value
            q = q.next
            s.next = q
        else:
            q = q.next
            s = s.next
            last = q.value
    if p.next.value % p.value == 0:
        p = p.next
    return p


# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
def p15_check_number_of_ones(p):
    if p is None:
        return

    def number_of_ones_greater_than_twos_in_3_system(x):
        if x == 1:
            return 1
        res1 = res2 = 0
        while x > 0:
            if x % 3 == 1:
                res1 += 1
            elif x % 3 == 2:
                res2 += 1
            x //= 3
        return res1 > res2

    s = q = p
    q = q.next
    while q is not None:
        if number_of_ones_greater_than_twos_in_3_system(q.value):
            q = q.next
            s.next = q
        else:
            q = q.next
            s = s.next

    if number_of_ones_greater_than_twos_in_3_system(p.value):
        p = p.next
    return p


# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.
def p16_reorder_list(p):
    if p is None:
        return

    def nun_of_5_in_8_system(x):
        res = 0
        while x > 0:
            if x % 8 == 5:
                res += 1
            x //= 8
        return res % 2 == 0

    s = q = p
    q = q.next
    while q is not None:
        if nun_of_5_in_8_system(q.value):
            s.next = q.next
            q.next = p
            p = q
            q = s.next
        else:
            q = q.next
            s = s.next
    return p


# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
def p17_delete_numbers_with_odd_1(p):
    if p is None:
        return

    def is_number_of_1_in_2_system_odd(x):
        res = 0
        while x > 0:
            if x % 2 == 1:
                res += 1
            x //= 2
        return res % 2 == 1

    if p.next is None:
        if is_number_of_1_in_2_system_odd(p.value):
            p = p.next
            return p
    s = q = p
    q = q.next
    while q is not None:
        if is_number_of_1_in_2_system_odd(q.value):
            s.next = q.next
            if q.next is not None:
                q.next.previous = s
            q = q.next
        else:
            q = q.next
            s = s.next
    if is_number_of_1_in_2_system_odd(p.value):
        p = p.next
    return p


# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
def p18_make_uniq_list(p):
    if p is None or p.next is None:
        return p
    tab = []
    s = q = p
    q = q.next
    tab.append(s.value)
    while q:
        if q.value not in tab:
            tab.append(q.value)
            q = q.next
            s = s.next
        else:
            s.next = q.next
            q = q.next
    return p


# 19. Elementy w liście są uporządkowane według wartości klucza. Proszę
# napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
# funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.
def p19_delete_not_uniq_elements(p):
    if p is None or p.next is None:
        return p
    tab = []
    s = q = p
    q = q.next
    tab.append(s.value)
    res = 0
    while q:
        if q.value not in tab:
            tab.append(q.value)
            q = q.next
            s = s.next
        else:
            res += 1
            s.next = q.next
            q = q.next
    return res


# 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
# podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
# najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
# dokładnie jednej najdłuższej podlisty rosnącej.
def p21_longest_increasing_list_deleted(p):
    if p is None or p.next is None:
        return None
    last = end = p
    first = start = None
    s = q = p
    max_len = 1
    curr_len = 1
    q = q.next
    while q:
        if q.value > s.value:
            curr_len += 1
        else:
            if curr_len > max_len:
                end = s
                first = start
                max_len = curr_len
                last = end
            start = end = s
            curr_len = 1
        q = q.next
        s = s.next
    if curr_len > max_len:
        first = start
        last = s
    if first is None:
        p = last.next
        return p
    first.next = last.next
    return p


# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.
def p22_has_cycle(p):
    if p is None or p.next is None:
        return False
    q = p.next
    if q.next == p:
        return True
    while q != p and q.next is not None and q.next.next is not None and p.next is not None:
        q = q.next.next
        p = p.next
    return q == p


# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.
def p23_nof_elements_in_cycle(p):
    if p is None or p.next is None:
        return 0
    q = p.next
    while q != p:
        q = q.next.next
        p = p.next
    res = 1
    p = p.next
    while p != q:
        res += 1
        p = p.next
    return res


# 24. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.
def p24_nof_elements_before_cycle(p):
    if p is None or p.next is None:
        return 0
    q = p.next
    p_mem = p
    while q != p:
        q = q.next.next
        p = p.next
    res = 0
    is_done = False
    while not is_done:
        q = p.next
        if p_mem == q:
            return res
        is_in_cycle = False
        while q != p:
            if p == p_mem:
                is_in_cycle = True
            p = p.next
        if is_in_cycle:
            return res
        else:
            res += 1
        p_mem = p_mem.next


# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.
def p25_last_node_before_cycle(p):
    if p is None or p.next is None:
        return 0
    q = p.next
    p_mem = p
    while q != p:
        q = q.next.next
        p = p.next

    q = p.next
    if p_mem == q:
        return None
    while q != p:
        if p == p_mem:
            return None
        p = p.next
    s = p_mem
    p_mem = p_mem.next
    is_done = False
    while not is_done:
        q = p.next
        if p_mem == q:
            return s
        is_in_cycle = False
        while q != p:
            if p == p_mem:
                is_in_cycle = True
            p = p.next
        if is_in_cycle:
            return s
        s = p_mem
        p_mem = p_mem.next


# p27 = p3

# 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
# nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
# listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.
def p28_delete_same_elements(p1, p2):
    if p1 is None and p2 is None:
        return None
    q1 = p1
    s = None
    q2 = p2
    res = 0
    while q2:
        q1 = p1
        s = None
        while q1 and q2.value > q1.value:
            s = q1
            q1 = q1.next
        k = q2
        q2 = q2.next
        if s is None:
            k.next = p1
            p1 = k
        else:
            l = s.next
            s.next = k
            k.next = l
    res = 0
    q = p1
    l = None
    last = None
    first = None
    cnt = 1
    while q:
        if q.value == last:
            cnt += 1
        else:
            if cnt >= 2:
                if first is None:
                    p1 = q
                else:
                    first.next = q
                res += cnt
            first = l
            last = q.value
            cnt = 1
        l = q
        q = q.next
    if cnt >= 2:
        first.next = None
        res += cnt
    print(res)
    return p1


# 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
# funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
# funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
# łączną liczbę usuniętych elementów.
def p29_delete_different_elements(p1, p2):
    if p1 is None and p2 is None:
        return None
    q1 = p1
    s = None
    q2 = p2
    res = 0
    while q2:
        q1 = p1
        s = None
        while q1 and q2.value > q1.value:
            s = q1
            q1 = q1.next
        k = q2
        q2 = q2.next
        if s is None:
            k.next = p1
            p1 = k
        else:
            l = s.next
            s.next = k
            k.next = l
    res = 0
    q = p1
    last = None
    first = None
    cnt = 1
    print_forward(p1)
    while q:
        if q.value == last:
            first = q
            cnt += 1
        else:
            if cnt == 1:
                if first is None:
                    p1 = q
                else:
                    first.next = q
                    res += 1
            last = q.value
            cnt = 1
        q = q.next
    if cnt == 1:
        first.next = None
        res += 1
    print(res)
    return p1


# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
# się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
# drugiej elementy występują w przypadkowej kolejności. Proszę napisać
# funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
def p30_make_uniq_list_from_two(p1, p2):
    # p1 is sorted
    q2 = p2
    p1 = p18_make_uniq_list(p1)
    while q2:
        s = r = p1
        r = r.next
        if q2.value < s.value:
            k = Node(q2.value)
            k.next = s
            p1 = k
        elif q2.value != s.value:
            while r and q2.value > r.value:
                s = r
                r = r.next
            if (r and q2.value != r.value) or (r is None and q2.value > s.value):
                s.next = Node(q2.value)
                s.next.next = r

        q2 = q2.next
    return p1


# p1 = Node()
# p1 = tab_to_list([4, -32, 64])
# p2 = Node()
# p2 = tab_to_list([9, 0, 9, 3, 0, 50, 50, 60, 70, 80, 99, 1])
# print_forward(p1)
# print()
# p1 = p14_delete_dividable_numbers(p1)
# print_forward(p1)

# def f1():
#
#     a = 5
#     def f2():
#         a = 10
#     f2()
#     print(a)
#
# f1()
