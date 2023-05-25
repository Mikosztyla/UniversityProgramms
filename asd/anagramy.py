def count(A, B, k):
    n = len(A)
    letters = [0 for _ in range(k)]
    for i in range(n):
        letters[A[i]] += 1
        letters[B[i]] -= 1
    for i in range(n):
        if letters[i] != 0:
            return False
    return True
