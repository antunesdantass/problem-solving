word = raw_input()
stack = []
turn = 0
for letter in word:
    stack.append(letter)
    if len(stack) >= 2:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            turn = 0 if turn == 1 else 1

print "Yes" if turn == 1 else "No"