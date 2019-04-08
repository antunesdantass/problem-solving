n = int(raw_input())
initialCompilation = sorted(raw_input().split())
first = sorted(raw_input().split())
second = sorted(raw_input().split())

dif1 = None
dif2 = None

for i in range(len(first)):
    if initialCompilation[i] != first[i]:
        dif1 = initialCompilation[i]
        break

for i in range(len(second)):
    if first[i] != second[i]:
        dif2 = first[i]
        break

dif1 = dif1 if dif1 != None else initialCompilation[-1]
dif2 = dif2 if dif2 != None else first[-1]

print dif1
print dif2