# Vasya and Arrays 

len1 = int(raw_input())
array1 = map(int, raw_input().split())
len2 = int(raw_input())
array2 = map(int, raw_input().split())

i, j = (0, 0)
counterI, counterJ = (array1[i], array2[j])

result = []

while i < len1 and j < len2:
    if counterI == counterJ:
        result.append(counterI)
        i += 1
        j += 1
        if i < len1 and j < len2:
            counterI = array1[i]
            counterJ = array2[j]
    elif counterI > counterJ:
        j += 1
        if j < len2:
            counterJ += array2[j]
    else:
        i += 1
        if i < len1:
            counterI += array1[i]
resultA = result[:]
resultB = result[:]

while i < len1:
    resultA.append(array1[i])
    i += 1
while j < len2:
    resultB.append(array2[j])
    j += 1

print len(resultA) if resultA == resultB else -1