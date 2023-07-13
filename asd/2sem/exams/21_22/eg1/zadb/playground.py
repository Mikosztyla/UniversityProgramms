class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def count_height_of_tree(T):
    levels = []

    def visit_node(n, level):
        if len(levels) == level:
            levels.append(1)
        else:
            levels[level] += 1
        if n.left:
            visit_node(n.left, level+1)
        if n.right:
            visit_node(n.right, level+1)

    visit_node(T, 0)
    return levels


def dfs_erase(T, level):
    result = 0

    def dfs_visit(n, l):
        nonlocal result
        if n is None:
            return l-1
        max_level_left = dfs_visit(n.left, l + 1)
        max_level_right = dfs_visit(n.right, l + 1)
        if l <= level:
            if max_level_left != level and n.left is not None:
                max_level_left = l
                result += 1
            if max_level_right != level and n.right is not None:
                result += 1
                max_level_right = l
        return max(max_level_right, max_level_left)

    dfs_visit(T, 0)
    return result


def wideentall( T ):
    levels = count_height_of_tree(T)
    max_value = levels[-1]
    max_index = len(levels)-1
    for i in range(len(levels)-1, -1, -1):
        if levels[i] > max_value:
            max_value = levels[i]
            max_index = i

    return dfs_erase(T, max_index)



A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G
print(wideentall(A))