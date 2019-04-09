from collections import deque

n, t, c = map(int, raw_input().split())
prisoners = map(int, raw_input().split())
possibilities = 0
deque = deque(maxlen=c)

for prison in prisoners:
    if prison <= t:
        deque.append(prison)
        if len(deque) == c:
            possibilities += 1
    else:
        deque.clear()

print possibilities