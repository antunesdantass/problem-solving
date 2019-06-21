a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

total = 0

while a > 0 and b >= 2 and c >= 4:
    a -= 1
    b -= 2
    c -= 4
    total += 7

print total