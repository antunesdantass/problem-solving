n = int(raw_input())
florescents = map(int, raw_input().split())
adj = { x: [] for x in range(1, n + 1) }

for i in range(1, n):
    adj[florescents[i - 1]].append(i + 1)

queue = adj[1]
count = 1
while len(queue) > 0:
    count += len(queue) % 2
    newQueue = []
    for i in queue:
        newQueue += adj[i]
    queue = newQueue

print count