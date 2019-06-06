n = int(raw_input())
balls = sorted(list(set(map(int, raw_input().split()))))
i = 0
j = 2
possible = False
while j < len(balls) and not possible:
    que = set(balls[i:j + 1])
    if abs(balls[i] - balls[j]) < 3 and len(set(balls[i:j + 1])) == 3:
        possible = True
    else:
        i += 1
        j += 1

print "YES" if possible else "NO"