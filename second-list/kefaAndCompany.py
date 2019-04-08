def getTuple(string):
    money, friendFactor = map(int, string.split())
    return (money, friendFactor)

nOfFriends, maxDiference = map(int, raw_input().split())
friendsData = [getTuple(raw_input()) for x in range(nOfFriends)]
friendsData.sort(key=lambda tup: tup[0])
maxInterval = 0
bestInterval = 0

i = 0
j = 0

while j < nOfFriends:
    if friendsData[j][0] - friendsData[i][0] < maxDiference:
        maxInterval += friendsData[j][1]
        j += 1
    else:
        bestInterval = maxInterval if maxInterval > bestInterval else bestInterval
        maxInterval -= friendsData[i][1]
        i += 1
    bestInterval = maxInterval if maxInterval > bestInterval else bestInterval

print bestInterval