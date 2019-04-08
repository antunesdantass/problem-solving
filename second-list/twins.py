numberOfCoins = int(raw_input())
coins = map(int, raw_input().split())
totalValue = sum(coins)
coins.sort(reverse=True)
acumulator = 0
i = 0
while acumulator < totalValue / 2.0:
    acumulator += coins[i]
    i += 1

print i