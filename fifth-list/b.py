# B - Pashmak and Flowers

nOfFlowers = int(raw_input())
flowers = map(int, raw_input().split())
maxFlower = flowers.count(max(flowers))
minFlower = flowers.count(min(flowers))
maxDifference = max(flowers) - min(flowers)
comb = maxFlower * minFlower if maxDifference > 0 else nOfFlowers * (nOfFlowers - 1) / 2
print "%i %i" % (maxDifference, comb)