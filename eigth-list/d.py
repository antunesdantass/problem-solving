# Fedor and New Game

n, m, k = map(int, raw_input().split())
soldiers = []
total = 0
for i in range(m + 1):
    soldiers.append(bin(int(raw_input()))[2:])
fedor = soldiers[-1]
for i in range(m):
    fedorFormated = fedor.zfill(max(len(fedor), len(soldiers[i])))
    soldier = soldiers[i].zfill(max(len(fedor), len(soldiers[i])))
    count = 0
    for j in range(-1, -1 * len(fedorFormated) - 1, -1):
        if fedorFormated[j] != soldier[j]:
            count += 1
    if count <= k:
        total += 1
    
print total