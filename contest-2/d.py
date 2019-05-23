n, k, q = map(int, raw_input().split())
temperatures = {}
for recipe in range(n):
    beg, end = map(int, raw_input().split())
    for temp in range (beg, end + 1):
        if temp not in temperatures:
            temperatures[temp] = 0
        temperatures[temp] += 1
possibles = []
for question in range(q):
    possible = 0
    beg, end = map(int, raw_input().split())
    for temp in range (beg, end + 1):
        if temp in temperatures and temperatures[temp] >= k:
            possible += 1
    possibles.append(str(possible))

print "\n".join(possibles)