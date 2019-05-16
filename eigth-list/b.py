# Finding Team Member

n = int(raw_input())
players = []
nth = 2
for i in range(2 * n - 1):
    pairs = map(int, raw_input().split())
    for j in range(len(pairs)):
        players.append((nth, j + 1, pairs[j]))
    nth += 1
players.sort(key=lambda item: item[2], reverse = True)
playersSet = set()
pairs = [0 for x in range(2 * n)]
i = 0
while len(playersSet) < 2 * n - 1:
    if players[i][0] not in playersSet and players[i][1] not in playersSet:
        playersSet.add(players[i][0])
        playersSet.add(players[i][1])
        pairs[players[i][0] - 1] = str(players[i][1])
        pairs[players[i][1] - 1] = str(players[i][0])
    i += 1

print " ".join(pairs)