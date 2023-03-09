def merge_sort(tab):
    if len(tab) <= 1:
        return
    middle = len(tab)//2
    left = tab[:middle]
    right = tab[middle:]
    merge_sort(left)
    merge_sort(right)

    i = j = 0
    for k in range(len(left)+len(right)):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
        elif i < len(left):
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1


tab = [4, 7, 3, 9, 4, 5, 2, 1, 6, 5, 4]
merge_sort(tab)
print(tab)