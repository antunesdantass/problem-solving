# Bear and Three Musketeers
import sys
raw_input = sys.stdin.readline

n, m = map(int, raw_input().split())
muskRel = { i: set() for i in range(1, n + 1) }
minimum = sys.maxint

for i in range(m):
    j, k = map(int, raw_input().split())
    muskRel[j].add(k)
    muskRel[k].add(j)

for i in range(1, n + 1):
    for j in muskRel[i]:
        for k in muskRel[j]:
            if k in muskRel[i]:
                knowledge = len(muskRel[i]) + len(muskRel[j]) + len(muskRel[k]) - 6
                minimum = knowledge if knowledge < minimum else minimum

print minimum if minimum != sys.maxint else -1