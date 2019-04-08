from collections import deque
queue = deque(maxlen=10**9)

def operate(i):
    op = i[0]
    if op == "1":
        queue.append(i[1])
    elif op == "2":
        len(queue) > 0 and queue.popleft()
    else:
        if len(queue) > 0:
            print queue[0]
        else:
            print "Empty!"

n = int(raw_input())
for i in range(n):
    operate(raw_input().split())