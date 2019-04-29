# F - Two Buttons

n, m = map(int, raw_input().split())
minimum = 0
while n < m:
    n *= 2
    minimum += 1
while n > m:
    n -= 1
    minimum += 1

print minimum