n, m = map(int, raw_input().split())
array = raw_input().split()
diffCount = []
numberset = set()
integers = [int(raw_input()) for x in range(m)]
for i in range(len(array) - 1, -1, -1):
    if (array[i] not in numberset):
        numberset.add(array[i])
    diffCount.append(len(numberset))

diffCount.reverse()        

print "\n".join([str(diffCount[i - 1]) for i in integers])