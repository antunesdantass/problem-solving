options = [7, 6, 5, 4, 3, 2]

def hasSolution(n, options, times):
	best = options[0]
	while best <= n:
		n -= best
		times += 1
	if n == 0:
		return times
	else:
		return times + 1
		
nqueries = int(raw_input())
queries = map(lambda x: int(raw_input()), range(nqueries))

for query in queries:
	print hasSolution(query, options, 0)
