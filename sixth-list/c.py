# Dominos 2
vis = set()
adj = {}

def dfs(node):
    vis.add(node)
    for vizinho in adj[node]:
        if vizinho not in vis:
            dfs(vizinho)


nOfTests = int(input())
answers = []
for i in range(nOfTests):
    n, m, l = list(map(int, input().split()))
    for domino in range(1, n + 1):
        adj[domino] = []
    for vertex in range(m):
        head, tail = list(map(int, input().split()))
        adj[head].append(tail)
    for fall in range(l):
        dfs(int(input()))
    answers.append(len(vis))
    vis = set()
    adj = {}

for answer in answers:
    print(answer)
