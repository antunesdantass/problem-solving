testCases = []

while int(raw_input()) != 0:
    testCases.append(map(int, raw_input().split()))

def canReorder(order):
    stack = []
    lastPassed = 0
    for car in order:
        if lastPassed + 1 == car:
            lastPassed += 1
        else:
            while len(stack) > 0 and stack[-1] == lastPassed + 1:
                lastPassed += 1
                stack.pop()
                if lastPassed + 1 == car:
                    lastPassed += 1
            if lastPassed < car:
                stack.append(car)
    while len(stack) > 0:
        if stack.pop() != lastPassed + 1:
            return "no"
        else:
            lastPassed += 1
    
    return "yes"

tests = map(canReorder, testCases)

for result in tests:
    print result