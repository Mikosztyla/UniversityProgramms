def ducks_counter(curr_duck, width_left, curr_height, res=[]):
    global ducks
    if curr_duck == len(ducks):
        if width_left >= 0:
            global max_height
            max_height = max(curr_height, max_height)
            if curr_height == 65:
                print(res)
        return
    if width_left < 0:
        curr_height -= ducks[curr_duck - 1][0]
        width_left += ducks[curr_duck - 1][1]
        res.pop(len(res)-1)
    ducks_counter(curr_duck + 1, width_left - ducks[curr_duck][1], curr_height + ducks[curr_duck][0], res+[curr_duck])
    ducks_counter(curr_duck + 1, width_left, curr_height, res)


n = 20
w_max = 50
max_height = 0
ducks = [[3, 2], [5, 4], [7, 6], [2, 1], [8, 5], [4, 3], [6, 7], [9, 9], [1, 2], [5, 4], [7, 6], [8, 8], [3, 3], [4, 5],
         [6, 7], [2, 1], [1, 2], [5, 4], [8, 6], [9, 8]]
ducks_counter(0, w_max, 0)
print(max_height)