n = int(raw_input())
s = int(raw_input())
disks = sorted([int(raw_input()) for i in range(n)], reverse=True)
nOfDrivers = 0
i = 0
while s > 0:
    s -= disks[i]
    i += 1

print i