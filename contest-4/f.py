idles, jobs = map(int, raw_input().split())
chosen = map(int, raw_input().split())
cost = map(int, raw_input().split())
tuples = sorted([(i, chosen[i], cost[i]) for i in range(idles)], key=lambda item: item[2], reverse=True)
jobsChosen = set()
idleChosen = set()
for tuple in tuples:
    if tuple[1] not in jobsChosen:
        jobsChosen.add(tuple[1])
        idleChosen.add(tuple[0])
nOfUnchosen = jobs - len(jobsChosen)
cost = 0
i = len(tuples) - 1
while nOfUnchosen > 0:
    if tuples[i][0] not in idleChosen:
        idleChosen.add(tuples[i][0])
        cost += tuples[i][2]
        nOfUnchosen -= 1
    i -= 1

print cost