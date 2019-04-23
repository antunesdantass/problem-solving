# Chocolate 

n = int(raw_input())
bar = map(int, raw_input().split())

total = 1
count = 0
pos = -1

for i in range(n):
    if bar[i] == 1:
        count += 1
        if count == 1:
            pos = i
        elif count == 2:
            total *= i - pos
            count = 1
            pos = i

print total if pos != -1 else 0