a, b = map(int, raw_input().split())
slices = [0 for x in range(16)]
i = 0
while a != 0 and b != 0 and i < 15:
    slices[i] = 0
    slices[i + 1] = 1
    a -= 1
    b -=1
    i += 2

while a > 0 and i < 15:
    slices[i] = 0
    a -= 1
    i += 2
 
while b > 0 and i < 15:
    slices[i] = 1
    b -= 1
    i += 2

print "Yay!" if a == 0 and b == 0 else ":("