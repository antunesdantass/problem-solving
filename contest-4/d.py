n = int(raw_input())
m = [int(x) for x in raw_input().split()]
a = 0
for i in m:
    while i % 2 == 0:
        i /= 2
        a += 1
print a