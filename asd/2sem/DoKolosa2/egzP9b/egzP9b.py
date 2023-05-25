from egzP9btesty import runtests


def euler(G):
	n = len(G)
	start_v = [0 for _ in range(n)]
	solution = []

	def dfs_visit(G, v):
		nonlocal solution
		n = len(G)
		for u in range(start_v[v], n):
			if G[v][u] >= 1:
				G[v][u] -= 1
				start_v[v] = u
				dfs_visit(G, u)
				solution.append(u)

	dfs_visit(G, 0)
	solution.append(0)
	solution = solution[::-1]
	return solution


def dyrektor(G, R):
	n = len(G)
	G2 = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for e in G[i]:
			if e not in R[i]:
				G2[i][e] += 1
			else:
				R[i].remove(e)

	return euler(G2)


runtests(dyrektor, all_tests=True)
