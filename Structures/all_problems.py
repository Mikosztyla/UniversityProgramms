# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.
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


def p9_decrease_number_by_1(p):
    if p is None:
        return
    r = p
    while r.next is not None:
        r = r.next
    r.value -= 1
    return p


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


p1 = Node()
p1 = tab_to_list([1, 4, 7, 9, 14, 35])
p2 = Node()
p2 = tab_to_list([9, 0, 9, 3, 0, 50, 50])
print_forward(p1)
print_forward(p2)
p1 = p30_make_uniq_list_from_two(p1, p2)
print_forward(p1)
