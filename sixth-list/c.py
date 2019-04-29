# Dominos 2

def verifyFalls(adj, node):
    count = 1
    while node in adj:
        count += 1
        node = adj[node][0]
    
    return count


nOfTests = int(input())
answers = []
for i in range(nOfTests):
    n, m, l = list(map(int, input().split()))
    adj = {}
    for vertex in range(m):
        head, tail = list(map(int, input().split()))
        if head not in adj:
            adj[head] = []
        adj[head].append(tail)
    total = 0
    for fall in range(l):
        total += verifyFalls(adj, int(input()))
    answers.append(total)

for answer in answers:
    print(answer)
