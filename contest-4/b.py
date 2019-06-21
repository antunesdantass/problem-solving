a = int(raw_input())
b = [x for x in raw_input()]
c = [x for x in raw_input()]
cost = 0
for i in range(a - 1):
    if b[i] != c[i]:
        if b[i+1] == c[i] and c[i+1] == b[i]:
            cost += 1
            b[i+1], b[i] = b[i], b[i+1]
        else:
            cost += 1
            b[i] = c[i]
if b[a - 1] != c[a - 1]:
    cost += 1

print cost