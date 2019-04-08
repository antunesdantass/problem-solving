numberOfStudents = int(raw_input())
skills = sorted(map(int, raw_input().split()))

i, j = 0, 0
largestTeam = 0

while j < numberOfStudents:
    if skills[j] - skills[i] <= 5:
        j += 1
    else:
        i += 1
    if (j - i > largestTeam):
        largestTeam = j - i
print largestTeam 