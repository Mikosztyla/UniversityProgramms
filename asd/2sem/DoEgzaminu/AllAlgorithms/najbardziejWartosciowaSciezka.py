from math import inf


class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None


n = 3
dp = [-inf for _ in range(n)]
