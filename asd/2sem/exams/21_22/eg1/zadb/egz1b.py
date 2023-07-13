from egz1btesty import runtests


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
        if n is None:
            return

        if n.left is not None:
            dfs_visit(n.left, l+1)
        if n.right is not None:
            dfs_visit(n.right, l+1)

        if n.left is None and n.right is None:
            n.x = True
        else:
            if n.left is not None and n.right is not None:
                n.x = n.left.x and n.right.x
            elif n.left is not None:
                n.x = n.left.x
            else:
                n.x = n.right.x

        if l == level:
            n.x = False

    dfs_visit(T, 0)

    def erase(n):
        nonlocal result
        if n.x:
            result += 1
        else:
            if n.left is not None:
                erase(n.left)
            if n.right is not None:
                erase(n.right)

    erase(T)
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

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )